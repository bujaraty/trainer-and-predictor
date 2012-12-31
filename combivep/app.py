import sys
import os
import numpy as np
import combivep.settings as combivep_settings
import combivep.preproc.dataset as combivep_dataset
import combivep.engine.wrapper as combivep_wrapper


def train_combivep_using_cvf_data(training_data_file, 
                                  params_out_file=combivep_settings.USER_PARAMETERS_FILE,
                                  random_seed=combivep_settings.DEFAULT_SEED,
                                  n_hidden_nodes=combivep_settings.DEFAULT_HIDDEN_NODES,
                                  figure_dir=combivep_settings.DEFAULT_FIGURE_DIR,
                                  iterations=combivep_settings.DEFAULT_ITERATIONS,
                                  config_file=combivep_settings.COMBIVEP_CONFIGURATION_FILE,
                                  ):
    """

    CVF (CombiVEP format) is a parsed format intended to be used by CombiVEP.
    CVF has 5 fields, CHROM, POS, REF, ALT, EFFECT (1=deleterious, 0=neutral). All are tab separated
    Required arguments
    - neutral_data_file : list of SNPs with no harmful effect, CVF format
    - pathognice_data_file : list of SNPs with deleterious effect, CVF format

    """
    #pre-processing dataset
    print >> sys.stderr, 'pre-processing dataset . . . . '
    dm = combivep_dataset.DataSetManager(config_file=config_file)
    dm.load_data(training_data_file, file_type=combivep_settings.FILE_TYPE_CVF)
    dm.validate_data()
    dm.calculate_scores()
    dm.set_shuffle_seed(random_seed)
    dm.shuffle_data()
    dm.partition_data()

    #partition data
    training_dataset      = dm.get_training_data() 
    validation_dataset    = dm.get_validation_data() 

    #train !!!
    print >> sys.stderr, 'Training combiner . . . . '
    trainer = combivep_wrapper.Trainer(training_dataset, validation_dataset, random_seed, n_hidden_nodes, figure_dir)
    trainer.train(iterations)
    if not os.path.exists(combivep_settings.USER_PARAMETERS_DIR):
        os.makedirs(combivep_settings.USER_PARAMETERS_DIR)
    trainer.export_best_parameters(params_out_file)

def predict_deleterious_probability(SNPs_file,
                                    params_file=combivep_settings.USER_PARAMETERS_FILE,
                                    file_type=combivep_settings.FILE_TYPE_VCF,
                                    output_file=None,
                                    config_file=combivep_settings.COMBIVEP_CONFIGURATION_FILE,
                                    ):
    """

    CVF (CombiVEP format) is a parsed format intended to be used by CombiVEP.
    CVF has 5 fields, CHROM, POS, REF, ALT, EFFECT (1=deleterious, 0=neutral). All are tab separated
    Required arguments
    - SNPs_file : list of SNPs to be predicted, can be either VCF or CVF (default is VCF)

    """
    #pre-processing test dataset
    print >> sys.stderr, 'pre-processing test dataset . . . . '
    dm = combivep_dataset.DataSetManager(config_file=config_file)
    dm.load_data(SNPs_file, file_type=file_type)
    dm.validate_data()
    dm.calculate_scores()

    #predict
    predictor = combivep_wrapper.Predictor()
    predictor.import_parameters(params_file=params_file)
    out = (np.array(predictor.predict(dm.dataset)).reshape(-1,))

    #print output
    if output_file is not None:
        sys.stdout = open(output_file, 'w')
    print >> sys.stdout, "#%s\t%s\t%s\t%s\t%s\t%s" % ("CHROM", "POS", "REF", "ALT", "ACTUAL_DELETERIOUS_EFFECT", "PREDICTED_DELETERIOUS_PROBABILITY")
    for i in xrange(len(dm.dataset)):
        print >> sys.stdout, "%s\t%s\t%s\t%s\t%s\t%6.4f" % (dm.dataset[i][combivep_settings.KEY_SNP_INFO_SECTION][combivep_settings.KEY_CHROM],
                                                        dm.dataset[i][combivep_settings.KEY_SNP_INFO_SECTION][combivep_settings.KEY_POS],
                                                        dm.dataset[i][combivep_settings.KEY_SNP_INFO_SECTION][combivep_settings.KEY_REF],
                                                        dm.dataset[i][combivep_settings.KEY_SNP_INFO_SECTION][combivep_settings.KEY_ALT],
                                                        dm.dataset[i][combivep_settings.KEY_PREDICTION_SECTION][combivep_settings.KEY_TARGETS],
                                                        out[i],
                                                        )
    sys.stdout = sys.__stdout__

