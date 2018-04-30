from keras.models import model_from_json
import coremltools
import os

with open(os.path.join('', 'model/saved_model.json'), 'r') as f:
    loaded_model_json = f.read()

    keras_model = model_from_json(loaded_model_json)
    keras_model.load_weights(os.path.join('', 'model/model_weights.h5'))

    # convert model to Core ML
    coreml_model = coremltools.converters.keras.convert(keras_model, input_names='input', output_names='output')

    # set general model metadata
    coreml_model.author = 'Aleksei Degtiarev'
    coreml_model.license = 'BSD'
    coreml_model.short_description = 'Predicts the activity of the user: walking or falling'

    # set model input information
    coreml_model.input_description['input'] = 'AccX samples'

    # set model output information
    coreml_model.output_description['output'] = 'Activity'

    f_name, f_ext = os.path.splitext('model/model')
    coreml_model.save(os.path.join('', f_name + 'myCOREML'))
