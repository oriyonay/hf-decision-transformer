import subprocess 
# env_list = ["hopper-medium-expert-v2", "hopper-medium-replay-v2","walker2d-medium-replay-v2", "walker2d-medium-expert-v2", "antmaze-medium-play-v2",  "hammer-human-v1", "hammer-cloned-v1"]
env_list = [ "walker2d-medium-expert-v2", "antmaze-medium-play-v2",  "hammer-human-v1", "hammer-cloned-v1"]

for env in env_list:
    subprocess.run([
    "python", "-m", "experiment",
    "--env", f"{env}", 
    # "--num_eval_episodes", "10",
    "--log_to_wandb",
    "--embed_hf", "True", 
    "--hf_model_path", f"pref_model/model_{env}.pkl", 
    "--from_d4rl", "True",
    "--replay", "True",
    "--save_model", "True",
])
