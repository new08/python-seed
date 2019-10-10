## setting anaconda

### config

**换国内源**

 ```shell script
# 添加清华源   
conda config --add channels https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/free/    
conda config --add channels https://mirrors.tuna.tsinghua.edu.cn/anaconda/cloud/conda-forge    
conda config --add channels https://mirrors.tuna.tsinghua.edu.cn/anaconda/cloud/msys2/   

# 添加中科大源   
conda config --add channels https://mirrors.ustc.edu.cn/anaconda/pkgs/main/    
conda config --add channels https://mirrors.ustc.edu.cn/anaconda/pkgs/free/    
conda config --add channels https://mirrors.ustc.edu.cn/anaconda/cloud/conda-forge/    
conda config --add channels https://mirrors.ustc.edu.cn/anaconda/cloud/msys2/    
conda config --add channels https://mirrors.ustc.edu.cn/anaconda/cloud/bioconda/    
conda config --add channels https://mirrors.ustc.edu.cn/anaconda/cloud/menpo/    

# 设置搜索时显示通道地址   
conda config --set show_channel_urls yes    
 ```

**删源**
```shell script
conda config --remove-key channels
```