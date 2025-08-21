import sys
import subprocess


def getCmd(hasGPU=False):
    cmd = [sys.executable, '-m', 'pip', 'install',
           'setuptools',
           'd2l',
           ]
    if hasGPU:
        cmd.append('torch')
        cmd.append('torchvision')
        cmd.append('--index-url')
        cmd.append('https://download.pytorch.org/whl/cu129')
    else:
        cmd.append('torch')
        cmd.append('torchvision')
    return cmd


cmd = getCmd(False)
print(f'代码指令是: {" ".join(cmd)}')
print('=' * 100)
subprocess.run(cmd, check=True)
