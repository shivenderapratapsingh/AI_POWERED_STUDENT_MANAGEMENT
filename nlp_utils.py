from textblob import TextBlob


#Sentiment Analysis Function
def analyse_sentiment(text: str):
    blob=TextBlob(text)
    polarity=blob.sentiment.polarity

    #POLARITY[-1 AND 1]
    if polarity > 0:
        sentiment="POSITIVE 😊"
    elif polarity < 0:
        sentiment="NEGATIVE 😒"
    else:
        sentiment="NEUTRAL 😐"
    
    return{
        "polarity":polarity, 
        "sentiment":sentiment
    }
#Smart Search Function ()
def smart_search(students,query:str):
    query=query.lower()
    result=[]

    for student in students:
        if(query in student.name.lower() or query in student.course.lower()):
            result.append(student)
    return result

