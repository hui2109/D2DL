import sys
import subprocess
import json

commonCmd = [sys.executable, '-m', 'pip', 'install',
             'setuptools',
             'd2l',
             ]


def installPackages():
    with open('./localConfig.json', 'r', 1, 'utf-8') as f:
        localConfig = json.load(f)

    print(f'commonCmd 代码指令是: {" ".join(commonCmd)}')
    print('=' * 100)
    subprocess.run(commonCmd, check=True)
    print('=' * 100)

    if localConfig['hasGPU']:
        torchCmd = [sys.executable, '-m', 'pip', 'install',
                    'torch',
                    'torchvision',
                    '--index-url',
                    'https://download.pytorch.org/whl/cu129',
                    ]
    else:
        torchCmd = [sys.executable, '-m', 'pip', 'install',
                    'torch',
                    'torchvision',
                    ]

    print(f'torchCmd 代码指令是: {" ".join(torchCmd)}')
    print('=' * 100)
    subprocess.run(torchCmd, check=True)


if __name__ == '__main__':
    installPackages()
