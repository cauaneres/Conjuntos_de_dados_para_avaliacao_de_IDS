from nfstream import NFStreamer

online_streamer = NFStreamer(source="<rede>", statistical_analysis = True, idle_timeout=60, active_timeout=600)

total_flows_count = online_streamer.to_csv(path="same_attacks.csv", columns_to_anonymize=[], flows_per_file=0, rotate_files=0)