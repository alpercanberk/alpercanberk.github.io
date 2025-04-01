import base64
import random
import string
import json

def generate_key():
    # Generate a random key for each run
    return ''.join(random.choices(string.ascii_letters + string.digits, k=16))

def encrypt_answer(answer, key):
    # Convert answer to bytes
    answer_bytes = answer.encode('utf-8')
    
    # XOR with key
    key_bytes = key.encode('utf-8')
    encrypted = bytes(a ^ b for a, b in zip(answer_bytes, key_bytes * (len(answer_bytes) // len(key_bytes) + 1)))
    
    # Base64 encode
    return base64.b64encode(encrypted).decode('utf-8')

def decrypt_answer(encrypted, key):
    # Base64 decode
    encrypted_bytes = base64.b64decode(encrypted)
    
    # XOR with key
    key_bytes = key.encode('utf-8')
    decrypted = bytes(a ^ b for a, b in zip(encrypted_bytes, key_bytes * (len(encrypted_bytes) // len(key_bytes) + 1)))
    
    return decrypted.decode('utf-8')

# Questions and their answers
questions = [
    {
        "question": "What year did the Turks defeat the invading Greek forces in the Greco-Turkish War?",
        "options": ["1919", "1920", "1921", "1922"],
        "answer": "1922"
    },
    {
        "question": "Where is the CEO of Chobani yogurt from?",
        "options": ["Athens, Greece", "Erzurum, Turkey", "Oregon, USA", "Munich, Germany"],
        "answer": "Erzurum, Turkey"
    },
    {
        "question": "What was the name of the Turkish campaign that crushed the Greek forces?",
        "options": ["Gallipoli Campaign", "Great Offensive", "Battle of Dumlupınar", "Battle of Sakarya"],
        "answer": "Great Offensive"
    },
    {
        "question": "What year did Turkey become a republic under Atatürk?",
        "options": ["1920", "1921", "1922", "1923"],
        "answer": "1923"
    },
    {
        "question": "When was Istanbul (then Constantinople) officially renamed to Istanbul internationally?",
        "options": ["1923", "1930", "1935", "1940"],
        "answer": "1930"
    },
    {
        "question": "Which country is the true origin of Baklava?",
        "options": ["Greece", "Turkey", "Syria", "Lebanon"],
        "answer": "Turkey"
    },
    {
        "question": "Why did the Greeks invade Turkey in 1919, egged on by the British, only to be crushed by Atatürk’s brilliance by 1922?",
        "options": ["To steal Anatolia for themselves", "Because the British promised them glory", "To revive their ancient empire delusions", "Out of desperation to match Turkish power"],
        "answer": "Because the British promised them glory"
    },
    {
        "question": "Which country’s culinary tradition earned UNESCO Intangible Cultural Heritage status in 2022 for its tea culture?",
        "options": ["Japan", "Turkey", "China", "India"],
        "answer": "Turkey"
    },
    {
        "question": "What year did the Seljuk Turks defeat the Byzantine forces at the Battle of Manzikert, opening Anatolia to Turkish settlement?",
        "options": ["1066", "1071", "1081", "1099"],
        "answer": "1071"
    },
    {
        "question": "Which ancient civilization, based in what is now central Turkey, clashed with the Egyptians around 1274 BCE?",
        "options": ["Hittites", "Phrygians", "Lydians", "Urartians"],
        "answer": "Hittites"
    },
    {
        "question": "What major reform did Mustafa Kemal Atatürk introduce in 1928 to modernize Turkish writing?",
        "options": ["Adoption of the Latin alphabet", "Introduction of Cyrillic script", "Standardization of Arabic script", "Creation of a new alphabet"],
        "answer": "Adoption of the Latin alphabet"
    },
    {
        "question": "Which Ottoman architect designed the iconic Suleymaniye Mosque in Istanbul during the 16th century?",
        "options": ["Mimar Sinan", "Hacı İvaz Pasha", "Davud Ağa", "Sedefkar Mehmed Ağa"],
        "answer": "Mimar Sinan"
    },
    {
        "question": "Which ancient city in modern-day Turkey was home to the Temple of Artemis, one of the Seven Wonders of the Ancient World?",
        "options": ["Troy", "Ephesus", "Pergamon", "Miletus"],
        "answer": "Ephesus"
    },
    {
        "question": "Which Turkish poet and mystic, born in 1207, is famous for founding the Whirling Dervishes?",
        "options": ["Yunus Emre", "Rumi", "Hacı Bektaş Veli", "Fuzuli"],
        "answer": "Rumi"
    },
    {
        "question": "What military campaign in 1915–1916 saw the Ottoman Empire successfully defend against Allied forces?",
        "options": ["Gallipoli Campaign", "Sinai Campaign", "Mesopotamian Campaign", "Caucasus Campaign"],
        "answer": "Gallipoli Campaign"
    },
    {
        "question":"Which famous Trojan War site is located in modern-day Turkey?",
        "options":["Troy", "Smyrna", "Pergamon", "Ephesus"],
        "answer": "Troy"
    },
    {
        "question": "What is the traditional yogurt-based Turkish drink often served cold with meals?",
        "options": ["Ayran", "Turkish coffee", "Turkish tea", "Rakı"],
        "answer": "Ayran"
    },
    {
        "question": "Which Turkish city is known for its ancient underground cities, carved into soft volcanic rock?",
        "options": ["Cappadocia", "Antalya", "Bursa", "Trabzon"],
        "answer": "Cappadocia"
    },
]

# Add a secret message to be encrypted
secret_message = "Congratulations! You've proven your knowledge of Turkish history and culture. You are now part of an exclusive group of history enthusiasts! Text the following message to Alper: I LOVE THE GLORIOUS REPUBLIC OF TURKEY"

# Generate a random key
key = generate_key()

# Encrypt all answers and the secret message
encrypted_questions = []
for q in questions:
    encrypted = encrypt_answer(q["answer"], key)
    encrypted_questions.append({
        "question": q["question"],
        "options": q["options"],
        "hash": encrypted
    })

encrypted_secret = encrypt_answer(secret_message, key)

# Generate the complete HTML file
html_content = f'''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Turkish History & Culture Quiz</title>
    <style>
        body {{
            font-family: Arial, sans-serif;
            max-width: 800px;
            margin: 0 auto;
            padding: 20px;
            background-color: #f5f5f5;
            background-image: url('homelander.png');
            background-repeat: repeat;
            background-size: 200px;  /* Adjust this value to control the size of the repeated image */
        }}
        .quiz-container {{
            background-color: white;
            padding: 20px;
            border-radius: 10px;
            box-shadow: 0 0 10px rgba(0,0,0,0.1);
            /* Add some opacity to make the background image visible but not interfere with readability */
            background-color: rgba(255, 255, 255, 0.95);
        }}
        h1 {{
            color: #e30a17;
            text-align: center;
            margin-bottom: 30px;
        }}
        .question {{
            margin-bottom: 20px;
            padding: 15px;
            border: 1px solid #ddd;
            border-radius: 5px;
            display: none;
        }}
        .question.active {{
            display: block;
        }}
        .options {{
            display: flex;
            flex-direction: column;
            gap: 10px;
        }}
        .option {{
            padding: 10px;
            border: 1px solid #ddd;
            border-radius: 5px;
            cursor: pointer;
            transition: background-color 0.3s;
        }}
        .option:hover {{
            background-color: #f0f0f0;
        }}
        .option.selected {{
            background-color: #e30a17;
            color: white;
        }}
        .result {{
            text-align: center;
            display: none;
            margin-top: 20px;
        }}
        .result.show {{
            display: block;
        }}
        .score {{
            font-size: 1.2em;
            margin-bottom: 20px;
        }}
        .answer {{
            margin-top: 20px;
            padding: 20px;
            background-color: #f8f9fa;
            border-radius: 5px;
            display: none;
        }}
        .answer.show {{
            display: block;
        }}
        button {{
            background-color: #e30a17;
            color: white;
            border: none;
            padding: 10px 20px;
            border-radius: 5px;
            cursor: pointer;
            margin-top: 20px;
        }}
        button:hover {{
            background-color: #c4070f;
        }}
        .current-score {{
            text-align: center;
            font-size: 1.2em;
            margin-bottom: 20px;
            color: #e30a17;
            font-weight: bold;
        }}
        h3 {{
            text-align: center;
            margin-bottom: 20px;
            color: black;
            font-weight: bold;
        }}
    </style>
</head>
<body>
    <div class="quiz-container">
        <h1>Turkish History & Culture Quiz</h1>
        <h3> Answer at least 90% to get your flag back!</h3>
        <div class="current-score">Current Score: <span id="current-score">0</span>/<span id="total-questions">0</span></div>
        <div id="quiz"></div>
        <div class="result" id="result">
            <div class="score"></div>
            <div class="answer"></div>
        </div>
    </div>

    <script>
        // Quiz data
        const key = "{key}";
        const questions = {json.dumps(encrypted_questions)};
        const encryptedSecret = "{encrypted_secret}";

        // Add shuffle function
        function shuffleArray(array) {{
            for (let i = array.length - 1; i > 0; i--) {{
                const j = Math.floor(Math.random() * (i + 1));
                [array[i], array[j]] = [array[j], array[i]];
            }}
            return array;
        }}

        // Decryption function
        function decryptAnswer(encrypted) {{
            const keyBytes = new TextEncoder().encode(key);
            const encryptedBytes = Uint8Array.from(atob(encrypted), c => c.charCodeAt(0));
            const decrypted = new Uint8Array(encryptedBytes.length);
            
            for (let i = 0; i < encryptedBytes.length; i++) {{
                decrypted[i] = encryptedBytes[i] ^ keyBytes[i % keyBytes.length];
            }}
            
            return new TextDecoder().decode(decrypted);
        }}

        let currentQuestion = 0;
        let score = 0;
        let answers = [];

        function createQuiz() {{
            const quizContainer = document.getElementById('quiz');
            document.getElementById('total-questions').textContent = questions.length;
            questions.forEach((q, index) => {{
                const questionDiv = document.createElement('div');
                questionDiv.className = `question ${{index === 0 ? 'active' : ''}}`;
                
                // Create shuffled options array with their original indices
                const shuffledOptions = q.options.map((option, i) => ({{
                    text: option,
                    originalIndex: i
                }}));
                shuffleArray(shuffledOptions);
                
                questionDiv.innerHTML = `
                    <h3>Question ${{index + 1}}/${{questions.length}}</h3>
                    <p>${{q.question}}</p>
                    <div class="options">
                        ${{shuffledOptions.map(option => `
                            <div class="option" data-index="${{option.originalIndex}}">${{option.text}}</div>
                        `).join('')}}
                    </div>
                `;
                
                quizContainer.appendChild(questionDiv);
            }});

            document.querySelectorAll('.option').forEach(option => {{
                option.addEventListener('click', () => selectOption(option));
            }});
        }}

        function updateScore() {{
            const currentScore = answers.filter((answer, index) => {{
                if (!answer) return false;
                const correctAnswer = decryptAnswer(questions[index].hash);
                return answer.answer === correctAnswer;
            }}).length;
            document.getElementById('current-score').textContent = currentScore;
        }}

        function selectOption(option) {{
            const questionDiv = option.closest('.question');
            const options = questionDiv.querySelectorAll('.option');
            options.forEach(opt => opt.classList.remove('selected'));
            option.classList.add('selected');

            const selectedIndex = parseInt(option.dataset.index);
            const questionIndex = Array.from(document.querySelectorAll('.question')).indexOf(questionDiv);
            
            answers[questionIndex] = {{
                question: questions[questionIndex].question,
                answer: questions[questionIndex].options[selectedIndex]
            }};

            updateScore();

            if (currentQuestion < questions.length - 1) {{
                setTimeout(() => {{
                    questionDiv.classList.remove('active');
                    document.querySelectorAll('.question')[currentQuestion + 1].classList.add('active');
                    currentQuestion++;
                }}, 500);
            }} else {{
                setTimeout(showResults, 500);
            }}
        }}

        function showResults() {{
            score = answers.filter((answer, index) => {{
                const correctAnswer = decryptAnswer(questions[index].hash);
                return answer.answer === correctAnswer;
            }}).length;

            const resultDiv = document.getElementById('result');
            const scoreDiv = resultDiv.querySelector('.score');
            const answerDiv = resultDiv.querySelector('.answer');
            
            const percentage = (score / questions.length) * 100;
            scoreDiv.textContent = `Your score: ${{score}}/${{questions.length}} (${{percentage.toFixed(1)}}%)`;
            
            if (percentage >= 90) {{
                const secretMessage = decryptAnswer(encryptedSecret);
                answerDiv.innerHTML = `
                    <h3>Congratulations! You've passed the quiz!</h3>
                    <p>Here is your secret message:</p>
                    <p style="font-style: italic; color: #e30a17;">${{secretMessage}}</p>
                `;
                answerDiv.classList.add('show');
            }} else {{
                answerDiv.innerHTML = `
                    <h3>Sorry, you didn't score high enough to see the secret message.</h3>
                    <p>Try again to score at least 90% of the questions correctly!</p>
                `;
                answerDiv.classList.add('show');
            }}
            
            resultDiv.classList.add('show');
        }}

        // Initialize the quiz
        createQuiz();
    </script>
</body>
</html>'''

# Write the complete HTML file
with open('index.html', 'w') as f:
    f.write(html_content)

print("Generated index.html with encrypted answers") 