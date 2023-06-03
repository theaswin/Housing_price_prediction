from collections import namedtuple
# Out put components

DataIngestionArtifact = namedtuple("DataIngestionArtifact",["train_file_path",
                                                            "test_file_path",
                                                            "is_ingested",
                                                            "message"])