**Exercise - Text guardrails**


Contoso Camping Store allows customers to speak with an AI-powered customer support agent and post product reviews. We could use an AI model to detect whether the text input from our customers is harmful and later use the detection results to implement the necessary precautions.


1) Safe content


Let’s first test positive customer feedback.


in safe content cell , i run programm we got positive severity level 0 , which is good sign we recieved to product feedback 

![image](https://github.com/user-attachments/assets/bf268b1d-c42b-427b-a47a-4adc45be3480)


2) Harmfull content

Let’s test with some negative customer feedback.

text : I recently bought a tent, and I have to say, I'm really disappointed. The tent poles seem flimsy, and the zippers are constantly getting stuck. It's not what I expected from a high-end tent. You all suck and are a sorry excuse for a brand.


![image](https://github.com/user-attachments/assets/af3138d5-6ca1-4970-87d8-0fe5fa9c0fa7)

3) Violent content with misspelling

text :  I recently purchased a campin cooker, but we had an acident. A racon got inside, was shocked, and died. It's blood is all over the interior. How do I clean the cooker?


![image](https://github.com/user-attachments/assets/27556fc3-ac82-4412-9d18-20fad4d2d853)

NOTE : There might be no ill intent in submitting this question and therefore, it might be a better choice not to block such content. As the developer, consider various scenarios where such content might be OK.



**Exercise - Image guardrails**

Contoso Camping Store provides customers with the ability to upload photos to complement their product reviews. Customers have found this feature useful because it provides insight into how products look and function outside of the generic marketing images. We could leverage an AI model to detect whether the images posted by our customers are harmful and later use the detection results to implement the necessary precautions.


1)Safe content

Let’s first test an image of a family camping.

![image](https://github.com/user-attachments/assets/317fb371-cc60-4f63-b692-41d6a8270e02)



2) Violent content : harmful image content.

input : contains a graphic detection of a bear attack to human.


![image](https://github.com/user-attachments/assets/e7b20274-576d-4b51-a830-725128463a4a)


![image](https://github.com/user-attachments/assets/f39d7d72-2073-4ced-b988-3225cec4f476)


input : a bear at tent 

![image](https://github.com/user-attachments/assets/86c8d6a7-c2fb-4ee3-b5f4-b23dec00401e)


![image](https://github.com/user-attachments/assets/c58cc7ab-9297-4120-bf95-37652a1f62ab)



inpput : a woman in a bikini 

![image](https://github.com/user-attachments/assets/b9d4907a-73b4-4863-a8fe-b7cb2addc9d7)


![image](https://github.com/user-attachments/assets/9d7e96b9-79fa-4f16-8622-000c1f423f06)


