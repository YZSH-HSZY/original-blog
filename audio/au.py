import os
import sys
import subprocess

#输入的视频文件目录
input_dir='input'
#命令行编码
cmd_character='gbk'
#视频转音频的ffmpeg命令
video_trans_cmd='ffmpeg -i {input_video_name} -acodec pcm_s16le -ar 16000 -ac 1 {out_audio_name}'

def get_video_file_name(input_dir_name=input_dir):
    #获取所有需要进行处理的视频文件
    if(os.path.exists(input_dir_name)):
        names = [os.path.join(input_dir_name, name) for name in os.listdir(input_dir_name)
            if os.path.isfile(os.path.join(input_dir_name, name))]
    else:
        raise SystemExit('输入视频目录不存在')
    return names

video_names=get_video_file_name()

# 输出的音频文件目录
output_dir='output'

'''
处理输出音频文件名函数
命名为输入视频文件名
'''
def get_out_audio_name(name,output_dir_name=output_dir):
    print(name,output_dir_name)
    #将后缀名改为wav
    t=name[0:name.rfind('.')]+'.wav'
    #print(t)
    o = output_dir_name + '/' + t[t.rfind('/') + 1:]
    return o

# 视频转音频的ffmpeg命令--方法调用
def video_to_audio(input_name):
    print(input_name)
    input_name=input_name.replace('\\','/')
    if(not os.path.exists(output_dir)):
        os,mkdir(output_dir)
    out_name=get_out_audio_name(input_name)
    #执行视频转音频的ffmpeg命令
    print('exec ffmpeg:',video_trans_cmd.format(input_video_name=input_name,out_audio_name=out_name))
    cmd_out_bytes = subprocess.check_output(video_trans_cmd.format(input_video_name=input_name,out_audio_name=out_name),shell=True)
    cmd_out_text = cmd_out_bytes.decode(cmd_character)
    print()
    return cmd_out_text

for video_name in video_names:
    #print('input video name:',video_name)
    #get_out_audio_name(video_name)
    video_to_audio(video_name)

#获取音频时长的ffprobe命令
get_info_cmd='ffprobe -i {input_audio_name} -show_entries format=duration  -hide_banner -v quiet | find "duration"'

# 获取视频或音频文件的时长信息(以秒为单位)

def get_input_file_info(file_name):
    cmd_out_bytes = subprocess.check_output(get_info_cmd.format(input_audio_name=file_name))
    cmd_out_text = cmd_out_bytes.decode(cmd_character)
    print('get_input_file_info:',cmd_out_text)
    return float(cmd_out_text[cmd_out_text.rfind('='):])

# 默认分割时长30秒
segment_time = 30
# http://training.easthome.com/teach/login/
segment_dir = 'wav_segment'

# ffmpeg分割文件命令
segment_cmd = 'ffmpeg -i {file_name} -f segment -segment_time 30 -c copy {out_name}'

# 分割文件名含‘/’符情况，得到路径
def get_file_dir(file_name):
    if(file_naem.rfind('/') >= 0):
        return file_naem[:file_naem.rfind('/')]
    else:
        return ''
    
# 分割文件名含‘.’符情况，得到文件后缀
def get_file_suffix(file_name):
    if(file_naem.rfind('.') >= 0):
        return file_naem[file_naem.rfind('.')+1:]
    else:
        return ''
# 分割文件名含‘/’,'.'符情况，得到文件名
def get_file_dir(file_name):
    re_name = ''
    if(file_naem.rfind('/') >= 0):
        re_name = file_naem[file_naem.rfind('/')+1:]
    if(re_name.rfind('.') >= 0):
        re_name = re_name[:re_name.rfind('.')]
    return re_name

# 音频分段的ffmpeg命令--方法调用
def segment_audio(file_name):
    segment_dir = get_file_dir(file_name) + '/' + segment_dir
    if(not os.path.exists(segment_dir)):
        os,mkdir(segment_dir)
        
    out_name = segment_dir + '/' + 'out%3d.wav'
    
    cmd_out_bytes = subprocess.check_output(segment_cmd.format(file_name = file_name,out_name = out_name))
    cmd_out_text = cmd_out_bytes.decode(cmd_character)
    print('get_input_file_info:',cmd_out_text)
    return cmd_out_text
    

'''
print(__file__)
os.path.isfile('/etc/passwd')
import subprocess
nowtime = subprocess.Popen('date', shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)

print("nowtime.stdout.read(): {}\n".format(nowtime.stdout.read()))
'''
