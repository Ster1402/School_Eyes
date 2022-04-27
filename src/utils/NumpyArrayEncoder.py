import json
import numpy


"""
    To encode face encoding as str we need to :
    1- Get the face encoding : 
        img = face_recognition.load_image(<img_path>)
        face_encoding = face_recongnition.face_encodings(img)[0]
    2- Encode :
        face_encoding_str = json.dumps(face_encoding, cls=NumpyArrayEncoder)
        Then save as TEXT in database !
    3- Decode :
        Get face_encoding_str from database
        face_encoding = json.loads(face_encoding_str)

"""
class NumpyArrayEncoder(json.JSONEncoder):

    def default(self, obj):
        if isinstance(obj, numpy.integer):
            return int(obj)
        elif isinstance(obj, numpy.floating):
            return float(obj)
        elif isinstance(obj, numpy.ndarray):
            return obj.tolist()
        else:
            return super(NumpyArrayEncoder, self).default(obj)