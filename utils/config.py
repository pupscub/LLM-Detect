import multiprocessing

class Config:
    APEX = True # Automatic Precision Enabled
    BATCH_SCHEDULER = True
    BATCH_SIZE_TRAIN = 32
    BATCH_SIZE_VALID = 16
    BETAS = (0.9, 0.999)
    DEBUG = False
    DECODER_LR = 2e-5
    ENCODER_LR = 2e-5
    EPOCHS = 5
    EPS = 1e-6
    FOLDS = 4
    GRADIENT_ACCUMULATION_STEPS = 1
    GRADIENT_CHECKPOINTING = True
    MAX_GRAD_NORM=1000
    MAX_LEN = 512
    MIN_LR = 1e-6
    MODEL = "microsoft/deberta-v3-base"
    NUM_CYCLES = 0.5
    NUM_WARMUP_STEPS = 0
    NUM_WORKERS = multiprocessing.cpu_count()
    PRINT_FREQ = 20
    SCHEDULER = 'cosine' # ['linear', 'cosine']
    SEED = 27
    TRAIN = True
    TRAIN_FOLDS = [0, 1, 2, 3]
    WANDB = True
    WEIGHT_DECAY = 0.01


if Config.DEBUG:
    config.EPOCHS = 2
    config.TRAIN_FOLDS = [0]
