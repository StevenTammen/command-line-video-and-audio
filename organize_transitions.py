from lib.organize import *

current_dir_path = os.getcwd()
topic_transitions_dir_path = current_dir_path +'/topic-transitions'
rename_topic_transition_segments_to_be_in_tens(topic_transitions_dir_path)
