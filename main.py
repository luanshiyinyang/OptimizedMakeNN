# -*-coding:utf-8-*-
"""
author: luanshiyinyang
time: 2019-05-16 21:00:00
"""
import os
from argparse import ArgumentParser
from string import Template


def parse_param():
    """
    解析命令行传递参数
    :return:
    """
    ap = ArgumentParser()
    ap.add_argument('-c', '--config', default='config/config.txt', help='path of config file, like config.txt')
    ap.add_argument('-i', '--input', default='', help='path of input file about how to make NN')
    ap.add_argument('-o', '--output', default='output/output.png', help='path of output picture file')
    args_ = vars(ap.parse_args())
    return args_


def parse_nn_config(file_path):
    """
    解析配置
    :param file_path:
    :return:
    """
    rst = dict()
    with open(file_path, 'r', encoding='utf-8') as f:
        line = f.readline()
        layer_index = 0
        layers = list()
        nodes_num = []
        connections = []
        while line:
            if line[0] != '#':
                # 读取非注释行
                line_content = line.strip().split(',')
                node_num, layer = make_layer(line_content, layer_index)

                layers.append(layer)
                connections.append(line_content[-1])
                nodes_num.append(node_num)
                layer_index += 1
            line = f.readline()
    connect_rst = []
    for i in range(len(nodes_num)):
        connect_rst += make_connection(connections[i], i, nodes_num)
    rst['layers'] = layers
    rst['connections'] = connect_rst
    return rst


def make_layer(line: list, layer_index):
    """
    根据node行创建node
    :param line:
    :return:
    """
    template = Template(
        '''subgraph cluster_$layer_index {
           color=white;
           node [style=solid,color=$color, shape=circle];
           $nodes;
           label = "$label";
         }
        ''')
    node_num = int(line[1])
    nodes = list()
    for i in range(node_num):
        nodes.append('node{}_{}'.format(layer_index, i))
    nodes_str = ' '.join(nodes)
    layer = template.substitute(layer_index=layer_index, color=line[2], nodes=nodes_str, label=line[0])
    return len(nodes), layer


def make_connection(connect_desc: str, layer_index, node_num):
    """
    创建相邻两层连接，当然也可以不相邻，一般网络结构不是这样
    :return:
    """
    template = Template(
        '''
        $start -> $end
        '''
    )
    rst = []
    connect_desc = connect_desc[1:-1].split('=')
    if connect_desc[0] == '(all->all)':
        # 表示全连接
        for i in range(node_num[layer_index]):
            for j in range(node_num[layer_index+1]):
                rst.append(template.substitute(start='node{}_{}'.format(layer_index, i),
                                               end='node{}_{}'.format(layer_index+1, j)))
    elif connect_desc[0] == '(None->None)':
        # 表示无连接
        return []
    else:
        # 指定连接
        for connection in connect_desc:
            rst.append(connection[1:-1])
    return rst


def make_graph(config_dict):
    """
    生成graphviz语法结构文件
    :param config_dict:
    :return:
    """
    template = Template(
        '''digraph G {
            rankdir=LR
            splines=line
            nodesep=.05;
            node [label=""];
            
            $layers
            
            $connections
            }
        '''
    )

    rst = template.substitute(layers="\n".join(config_dict['layers']),
                              connections="\n".join(config_dict['connections']))
    return rst


def make_gv(path, content):
    """
    生成gv文件
    :return:
    """
    with open(path, 'w', encoding='utf-8') as f:
        f.write(content)
    print("generate gv file")


def make_pic(input_path, output_path):
    """
    生成输出图片
    :param path:
    :return:
    """
    path = output_path.split('/')
    if len(path) > 1:
        if not os.path.exists(path[0]):
            os.mkdir(path[0])
    cmd = 'dot ' + input_path + ' -Tpng -o ' + output_path
    os.system(cmd)
    print("generate pic")


if __name__ == "__main__":
    args = parse_param()  # 解析命令行参数

    if args['input'] != '':
        make_pic(args['input'], args['output'])
    else:
        args['input'] = 'config/nn.gv'
        nn_config = parse_nn_config(args['config'])
        gv_file = make_graph(nn_config)
        make_gv(args['input'], gv_file)
        make_pic(args['input'], args['output'])
