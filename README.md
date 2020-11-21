# Capstone_Project
Springboard Capstone Project : Text Summarization


About the dataset :
The DeepMind Q&A Dataset is a large collection of news articles from CNN and the Daily Mail with associated questions.
The dataset was developed for deep learning purpose and was presented in the 2015 paper “Teaching Machines to Read and Comprehend.”


Link to the Dataset : https://cs.nyu.edu/~kcho/DMQA/
Link to how the dataset was created by the original authors : https://github.com/deepmind/rc-data

Steps to install and run the project:


Requirements (minimum versions): 

  multiprocess==0.70.9
  numpy==1.17.2
  pyrouge==0.1.3
  pytorch-transformers==1.2.0
  tensorboardX==1.9
  torch==1.1.0
  
Tested and run on : AWS Deep Learning AMI (p2.xlarge) with source activate pytorch_latest_p37 
                    Installed PyRouge, pytorch-transformers and tensorboardX.
                    
Steps: 

1. Download the git repo
2. Change directory to : cd PreSumm/models
3. Download the pretrained Bert summmarization model from : https://drive.google.com/open?id=1kKWoV0QCbeIuFt85beQgJ4v0lujaXobJ
4. Unzip the model file
5. To run the model : 
     cd PreSumm
     python3 src/app.py 
 
To test the API :
Note : The model takes lomger to run the first time because it needs to download the BERT model from Hugging Face and caches it in PreSumm/temp folder.

I have used Postman for this purpose.

Sample queries : 

https://www.getpostman.com/collections/f5df53eb0493818a2e9e

GIF of running the above model :

![Demo](FinalDemo.gif)
