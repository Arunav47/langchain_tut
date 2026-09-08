from langchain_huggingface import HuggingFaceEmbeddings, HuggingFaceEndpointEmbeddings
from sklearn.metrics.pairwise import cosine_similarity
from dotenv import load_dotenv

load_dotenv()

new_var = 123
embedding_model = HuggingFaceEndpointEmbeddings(
    repo_id = "sentence-transformers/all-MiniLM-L6-v2",
    task= "feature-extraction"
)

document = [
    "Renewable energy sources such as solar, wind, and hydroelectric power are becoming increasingly popular as countries work to reduce carbon emissions. Solar panels convert sunlight into electricity, while wind turbines harness moving air to generate power. Although the initial installation costs can be high, renewable energy systems often save money over time because they require less fuel and maintenance compared to fossil fuel power plants.",

    "Artificial intelligence is transforming industries by automating repetitive tasks and assisting with complex decision-making. Machine learning models can analyze large amounts of data to detect patterns that humans might overlook. However, AI systems require high-quality data and careful monitoring to ensure fairness, reliability, and accurate predictions.",

    "Maintaining good health involves more than regular exercise. A balanced diet, sufficient sleep, and effective stress management all contribute to physical and mental well-being. People who consistently follow healthy habits are generally at a lower risk of developing chronic illnesses such as heart disease and diabetes.",

    "Space agencies continue to explore Mars in search of evidence that the planet may have once supported microbial life. Robotic rovers collect soil samples, capture high-resolution images, and analyze the planet's atmosphere. These missions also help scientists understand how future human exploration of Mars could become possible."
]


result = embedding_model.embed_documents(document)

questions = [
    "What kinds of data are collected on Mars?",
    "Which diseases are mentioned as preventable through healthy habits?",
    "Which industries benefit from artificial intelligence?",
    "Why are renewable energy systems cheaper in the long run?",

]

ques_embbedding = embedding_model.embed_documents(questions)

sim = cosine_similarity(ques_embbedding, result)

print(str(sim))

# for arr in sim:
#     question_index = arr.argmax()
#     print("Paragraph with the highest similarity to the question is: ", document[question_index])


