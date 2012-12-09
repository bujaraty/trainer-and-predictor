import numpy as np
import combivep.config as combivep_config
import combivep.engine.mlp as combivep_mlp


import matplotlib.pyplot as plt

class Trainer(combivep_mlp.Mlp):
    """This class is to produce parameter used by the Predictor class"""


    def __init__(self, training_dataset, validation_dataset, seed=None, n_hidden_nodes=4, figure_dir=None):
        combivep_mlp.Mlp.__init__(self, training_dataset.n_features, seed, n_hidden_nodes)

        self.__figure_dir = figure_dir
        self.__training_dataset   = training_dataset
        self.__validation_dataset = validation_dataset

    def train(self, iteration=10000):
        training_error   = []
        validation_error = []
        running_round    = 0
        best_validation_error = 0.99
        while True:
            out = self.forward_propagation(self.__training_dataset)
            self.backward_propagation(self.__training_dataset)
            weights1, weights2 = self.weight_update(self.__training_dataset)
            training_error.append(np.sum(np.absolute(self.calculate_error(out, 
                                                                          self.__training_dataset.targets
                                                                          )
                                                     ), 
                                         axis=1
                                         ).item(0) / self.__training_dataset.n_data)

            out = self.forward_propagation(self.__validation_dataset)
            validation_error.append(np.sum(np.absolute(self.calculate_error(out,
                                                                            self.__validation_dataset.targets
                                                                            )
                                                       ),
                                           axis=1
                                           ).item(0) / self.__validation_dataset.n_data)

            #check ending condition
            current_validation_error = validation_error[len(validation_error)-1]
            if (current_validation_error < combivep_config.MAXIMUM_ALLOWED_ERROR) and ((best_validation_error-current_validation_error) < combivep_config.MINIMUM_IMPROVEMENT):
                break

            #otherwise save parameters and record last error
            best_validation_error = validation_error[len(validation_error)-1]
            self.best_weights1 = weights1
            self.best_weights2 = weights2

            #check if it reach maximum iteration
            running_round += 1
            if running_round >= iteration:
                break

        if self.__figure_dir:
            print self.__figure_dir

    def __save_figure(self):
#        self.export_best_parameters('abc')
#        pt = plt.plot(training_error, label='training')
#        pv = plt.plot(validation_error, label='validation')
#        plt.legend(bbox_to_anchor=(0, 0, 0.98, 0.98), loc=1, borderaxespad=0.)
#        plt.show()
        pass

