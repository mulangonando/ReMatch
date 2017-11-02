Clone the Git

Install Python with the following requirements:

 Python 2.7
  
 NLTK (The later the better : Ensure you download Wordnet )
  
  Scikit-learn

Install PractNLP-tools

Most of the time, based on our experience (reported by few researchers), it is not possible to run our code locally due to some dependency problem, we are fixing this issue. Till then, we made a web service for this component. The Public endpoint for Rematch is: curl -d "Who is the wife of Barack Obama ? " http://94.130.104.232:8080. 
It has been recently pointed by several researchers that our code has performance issue and to answer each question, it takes more than 2 minutes. Soon, we will release newer version of code with lesser runtime. 
