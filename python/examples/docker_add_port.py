import argparse, os, json
# , and add port for a existing container


# parser.parse_known_args?
# docker 容器添加端口的python脚本
def get_or_set_file_content_json(file_path, model = 'r',content_json_str = None):
    if model.__eq__('w') and content_json_str != None:
        with open(os.path.join( os.path.dirname(__file__), file_path), 'wt') as f:
            f.write(content_json_str)
        return
    elif model.__eq__('w') and content_json_str == None:
        raise SystemExit('写配置文件未传入参数')
    with open(os.path.join( os.path.dirname(__file__), file_path), 'rt') as f:
        file_content_json = json.load(f)
    return file_content_json
'''
在hostconfig.json配置文件中添加映射端口
如果PortBindings不存在，则创建。存在则判断容器端口是否已映射
已映射，则添加映射规则，无创建
'''
def handle_add_port_config(file_content_json: dict, container_port_config: dict):
    # PortBindings不存在,创建PortBindings
    port_bindings = file_content_json.setdefault('PortBindings', {})
#     and isinstance(port_bindings, dict)
    # 将需要处理的容器映射端口container_port_config，添加入PortBindings项
    for key in container_port_config:
        # PortBindings子项容器映射端口不存在,创建
        port_bindings_key = port_bindings.setdefault(key, [])
        if len([n for n in port_bindings_key if n in container_port_config[key]]) != 0:
            raise SystemExit('添加端口映射已存在')
        port_bindings_key.extend(container_port_config[key])
    return file_content_json
#     file_content_json['PortBindings'] = {}
#     port_bindings = file_content_json['PortBindings']
#     port_bindings[container_port]
    
# 得到需要添加的映射端口选项
def get_need_container_port_info(container_port, host_port):
    container_port_str = container_port + '/' + args.protocol
    host_port_dict = {}
    host_port_dict['HostIp'] = ''
    host_port_dict['HostPort'] = str(host_port)
    return {str(container_port_str): [host_port_dict]}

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Change docker config file(hostconfig.json or config.v2.json)')
    # 添加需要处理的文件名列表,相对路径获取文件
    parser.add_argument(dest='filenames',metavar='filename', nargs='*', help='please input relative path')
    parser.add_argument('-p', '--ports',metavar='host_port:container_port',  dest='map_ports', action='append', help='need add port map')
    parser.add_argument('--protocol', dest='protocol', action='store', choices={'tcp','udp'}, 
                        default='tcp', help='select protocol default tcp')

    args, unknown = parser.parse_known_args()
    
    for port_map in args.map_ports:
        container_port, host_port = port_map.split(':')
        # 获取容器需要配置项
        container_port_config = get_need_container_port_info( container_port, host_port)
#         print (container_port_config)
        for file in args.filenames:
            # 添加配置
            print (handle_add_port_config(get_or_set_file_content_json(file), container_port_config))