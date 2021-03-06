# OptimizedMakeNN
- description
	- origin project from [https://github.com/rtygbwwwerr/MakeNN1.git](https://github.com/rtygbwwwerr/MakeNN1.git).
	- it is a mini tool for drawing a neural network graph by graphviz.
	- in this project, i optimize some code(from Python2 to Python3) for best use by command line.
- install
	- you can get this project by `git clone git@github.com:luanshiyinyang/OptimizedMakeNN.git`
	- please install graphviz in your computer
- instruction
	- in origin project from [rtygbwwwerr](https://github.com/rtygbwwwerr),you can use this command to draw net structure graphy
		- `python src/makeNN.py config.txt`
	- `config.txt` is figure structure of the configuration file, using utf-8 encoding modification can generate custom pictures.
		- **Here is actually the graphviz dot language neuron mapping mode do encapsulation, if very good at the dot language, you can use it directly to write scripts.**
		- Each line in this file represents a layer, and the format must follow the example in the config.txt file.（**Make sure the encoding is utf-8, and the punctuation is in English.**）
			- Name of the layer
			- number of neurons
			- color the neurons
			- this layer is connected to neurons in the next layer
				- node noden_m (such as the second node of input layer 1 to the second node of hidden layer 1, node0_1->node1_1)
				- all->all means full connection
				- none->None means connectionless, usually the last layer
	- command line arguments
		-  -i --input gv file (written in dot language, generated according to config.txt if no input)
		-  -c --config input script to generate gv files
		-  -o --output PNG picture directory (e.g. Output.rst.png, rst.png, etc.)
		- Attention
			- the above -i and -c conflict, do not enter at the same time (** or priority according to -i gv file to generate pictures **)
- samples
	- `python main.py --output rst.png`
	- config
		- ![](https://img-blog.csdnimg.cn/20190518132446125.png)
	- result
		- ![](https://img-blog.csdnimg.cn/20190518132505915.png)
- something more
	- This project is suitable for neuronal mapping, deep neural networks (such as convolutional neural networks), this tool is not suitable for you.
	- if you want to read README.md written by Chinese, please visit [README.md](https://github.com/luanshiyinyang/OptimizedMakeNN/blob/master/README-zh-cn.md).
	- Testing is currently done only in a Windows environment. This project started from my Github address, welcome star or fork.
