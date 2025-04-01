<?php
header('Content-Type: application/json');

// Store answers in a separate file that's not directly accessible
$answers = [
    "What year did the Turks defeat the invading Greek forces in the Greco-Turkish War?" => 3,
    "Where is the CEO of Chobani yogurt from?" => 1,
    "What was the name of the Turkish campaign that crushed the Greek forces?" => 1,
    "Which cuisine has UNESCO cultural heritage status?" => 0,
    "What year did Turkey become a republic under Atatürk?" => 3,
    "When was Istanbul (then Constantinople) officially renamed to Istanbul internationally?" => 1,
    "Which country is the true origin of Baklava?" => 1,
    "Where did Döner Kebab originate?" => 1
];

if ($_SERVER['REQUEST_METHOD'] === 'POST') {
    $data = json_decode(file_get_contents('php://input'), true);
    $userAnswers = $data['answers'] ?? [];
    
    $score = 0;
    foreach ($userAnswers as $question => $answer) {
        if (isset($answers[$question]) && $answers[$question] === $answer) {
            $score++;
        }
    }
    
    $totalQuestions = count($answers);
    $passed = $score >= 23;
    
    echo json_encode([
        'score' => $score,
        'total' => $totalQuestions,
        'passed' => $passed
    ]);
} else {
    http_response_code(405);
    echo json_encode(['error' => 'Method not allowed']);
}
?> 