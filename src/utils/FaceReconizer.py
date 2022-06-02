from PIL import Image
import face_recognition as fr

from ..model.Student import Student
from ..model.Discipline import Discipline


"""
    Argument sample:
        concerned_disciplines = [ { "name" :"GIT", 
                                    "axes" : ["GLO"] }, 
                                  { "name" : "TTIC", 
                                    "axes" : ["GI", "GRT"] } 
        ]
"""
class FaceReconizer:

    def __init__(self, concerned_disciplines: list, level: int) -> None:
        assert isinstance(concerned_disciplines, list)

        self.__disciplines = []
        self.__students = []
        print("[FaceReconizer.__init__]...")
        
        for discipline in concerned_disciplines:
            name = discipline["name"]
            axes = discipline["axes"]

            self.__disciplines.append( Discipline(name, axes, level) )
        
        self.__FindStudents()

        print("[FaceReconizer.__init__] : done !")

    def __FindStudents(self):

        for discipline in self.__disciplines:

            for axe in discipline["axes"]:

                students = axe["students"]
                #Tag all student with the axe name, discipline name and their level
                for i in range(len(students)):
                    students[i]["level"] = discipline["level"]
                    students[i]["axe_name"] = axe["name"]
                    students[i]["discipline_name"] = discipline["name"]

                self.__students.extend(students)

    def StudentsDetected(self, frame) -> list:

        print("[FaceReconizer.StudentsDetected]...")
        # pil_img = Image.fromarray(frame)
        # pil_img.show()
        # print("Showing frame...")

        result = set()

        try:
            face_locations = fr.face_locations(img=frame,
                                                model="hog", 
                                                number_of_times_to_upsample=3)
                
            print("[Face Locations]:", face_locations)

        except:
            print("Error while trying to get face locations")
            return set()

        else:

            if face_locations:
                unknowns_faces_encodings = fr.face_encodings(face_image=frame, 
                                                            known_face_locations=face_locations,
                                                            num_jitters=2)

            else:
                print("Nobody found with face_locations!")
                unknowns_faces_encodings = fr.face_encodings(face_image=frame,
                                                            num_jitters=2)
            

        for unknown_face_encoding in unknowns_faces_encodings:

            print("[Trying to know student]")

            for student in self.__students:
                
                print("[Comparing with : ", student["name"], "]")
                student_face_encodings = student["face_encodings"]

                if student_face_encodings:

                    matches = fr.compare_faces(known_face_encodings=student_face_encodings,
                                        face_encoding_to_check= unknown_face_encoding,
                                        tolerance=0.4)

                    number_of_match = matches.count(True)
                    print("Number of match:", number_of_match)

                    accurency_percent = (number_of_match / len(student_face_encodings))

                    print(f"Matches : {accurency_percent * 100}%")

                    #We add student if at least 40% of his pictures matches
                    if accurency_percent > 0.4:
                        #Remove face_encodings and pictures
                        s: Student = student.copy()
                        s["discipline_name"] = student["discipline_name"]
                        s["axe_name"] = student["axe_name"]
                        result.add(s)

        print("[FaceReconizer.StudentsDetected] : done !")

        return result
