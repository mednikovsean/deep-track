# Week 1: micrograd
- the gradient of the parameter is the derivative of the output (the loss in training a model) with respect to that parameter. it tells the rate and direction at which the output changes when that parameters value is nudged
- a mathematical depiction of a neuron includes a certain number of inputs to the neuron as well as weights that interact with each input. we multiply each input to its corresponding weight, these are then added together along with the bias of the neuron itself. this comprises the data value of the neuron. the output of the neuron passes this sum through an activation squashing function like tanh
- backpropogation is the method of finding the derivative (which is the gradient) of the output with respect to everyone of its inputs. we always start by finding the derivative of the output with respect to itself which is 1, we then fill in backwards (most confusing)
# Week 1: Huyen - Chapter 1: Introduction to Building AI Applications with Foundation Models
- if AI poses a threat to your business, you may want to do AI in-house instead of outsourcing to a competitor
- if you're using AI to boost profits and productivity you might have plenty of buy options that can save you time and money while giving you beyyer performance
- 3 layers of the AI stack: application development, model development, infrastructure
- AI Engineering - you use existing foundation models for your applications, you focus less on modeling and training and more on model adaptation
- AI engineering works with models that are bigger, consume more computer resources, and incur higher latency than traditional ML engineering (means more pressure for efficient training and inference optimization)
- ML engineering focuses on model development, AI engineering is more about adapting and evaulating models
- Prompt engineering means adapating a model without updated its weights, you give the model instructions and context instead of changing the model itself
- Finetuning, requires updating model weights, adapt model by making changes to it
- Pre-training - refers to training a model from scratch
- Finetuning - continuing to train a previously trained model
