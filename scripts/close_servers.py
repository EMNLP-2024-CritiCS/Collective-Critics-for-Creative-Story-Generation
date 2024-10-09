
import os
import sys

from storygen.common.server import ServerConfig


if __name__=='__main__':
    if not os.path.exists('server_configs.txt'):
        print('no server_configs.txt file found in current directory, exiting')
        sys.exit()
    user = os.environ['USER']
    processes = os.popen(f'ps -u {user} -f | grep vllm.entrypoints.openai.api_server').read().split('\n')
    if os.path.exists('server_configs.txt'):
        with open('server_configs.txt', 'r') as f:
            existing_configs = f.read().split('\n')
            existing_configs = [ServerConfig.from_json(config_str) for config_str in existing_configs if config_str != '']
    for process in processes:
        if process == '':
            continue
        for server_config in existing_configs:
            if f'--port {server_config.port}' in process:
                pid = process.split()[1]
                os.system(f'kill {pid} &')
                break
    os.system('rm server_configs.txt')