/* ---------------- TIMER LOGIC ---------------- */

let state = 'idle';
let startTime = 0;
let timerInterval = null;
let inspectionInterval = null;
let inspectionTime = 15;
let times = [];

const timer = document.getElementById('timer');
const timeEl = document.getElementById('time');
const timesEl = document.getElementById('times');

document.addEventListener('keydown', e => {
    if (e.code !== 'Space') return;
    e.preventDefault();

    if (state === 'idle') {
        startInspection();
    } 
    else if (state === 'running') {
        stopTimer();
    }
});

document.addEventListener('keyup', e => {
    if (e.code !== 'Space') return;
    e.preventDefault();

    if (state === 'ready') {
        startTimer();
    }
});


function startInspection() {
    state = 'inspection';
    timer.className = 'timer inspection';
    let t = inspectionTime;
    timeEl.textContent = t.toFixed(2);

    inspectionInterval = setInterval(() => {
        t -= 0.01;
        timeEl.textContent = t.toFixed(2);
        if (t <= 0) {
            clearInterval(inspectionInterval);
            timer.className = 'timer ready';
            timeEl.textContent = '0.00';
            state = 'ready';
        }
    }, 10);
}

function startTimer() {
    state = 'running';
    timer.className = 'timer running';
    startTime = Date.now();

    timerInterval = setInterval(() => {
        timeEl.textContent = ((Date.now() - startTime) / 1000).toFixed(2);
    }, 10);
}

function renderTimes() {
    timesEl.innerHTML = '';
    times.forEach(t => {
        const d = document.createElement('div');
        d.textContent = t.toFixed(2);
        timesEl.appendChild(d);
    });
}

function stopTimer() {
    clearInterval(timerInterval);
    state = 'idle';
    timer.className = 'timer idle';

    const finalTime = parseFloat(timeEl.textContent);

    times.unshift(finalTime);
    if (times.length > 5) times.pop();

    renderTimes();
    calculateAo5();
    saveSolve(finalTime);
}


function calculateAo5() {
    if (times.length < 5) {
        document.getElementById('avg').textContent = '-';
        return;
    }

    const sorted = [...times].sort((a, b) => a - b);
    const trimmed = sorted.slice(1, 4); // убрали лучший и худший
    const avg = trimmed.reduce((a, b) => a + b, 0) / 3;

    document.getElementById('avg').textContent = avg.toFixed(2);
}


/* ---------------- SAVE TO DJANGO ---------------- */

function saveSolve(time) {
    const form = document.getElementById('solve-form');
    const csrfToken = form.querySelector('[name=csrfmiddlewaretoken]').value;

    fetch(form.action, {
        method: 'POST',
        headers: {
            'X-CSRFToken': csrfToken,
            'Content-Type': 'application/x-www-form-urlencoded',
        },
        body: new URLSearchParams({
            cube_type: '2x2',
            scramble: document.getElementById('scramble-text').textContent,
            solve_time: time,
        }),
    });
}



/* INIT */
const scramble = document.getElementById('scramble-text').textContent;
renderCube(applyScramble(scramble));



/* ---------------- 2x2 CUBE LOGIC ---------------- */
function applyScramble(scramble) {
    resetCube();

    const moves = scramble.trim().split(/\s+/);

    moves.forEach(move => {
        switch (move) {
            case 'R': R(); break;
            case "R'": Rr(); break;
            case 'R2': R(); R(); break;

            case 'L': L(); break;
            case "L'": Lr(); break;
            case 'L2': L(); L(); break;

            case 'U': U(); break;
            case "U'": Ur(); break;
            case 'U2': U(); U(); break;

            case 'D': D(); break;
            case "D'": Dr(); break;
            case 'D2': D(); D(); break;

            case 'F': F(); break;
            case "F'": Fr(); break;
            case 'F2': F(); F(); break;

            case 'B': B(); break;
            case "B'": Br(); break;
            case 'B2': B(); B(); break;
        }
    });

    return cube;
}
function resetCube() {
    cube.U = [['Y','Y'],['Y','Y']];
    cube.D = [['W','W'],['W','W']];
    cube.F = [['G','G'],['G','G']];
    cube.B = [['B','B'],['B','B']];
    cube.R = [['O','O'],['O','O']];
    cube.L = [['R','R'],['R','R']];
}

const colorMap = {
    Y: '#FFD500',
    W: '#FFFFFF',
    G: '#009E60',
    B: '#0051BA',
    R: '#C41E3A',
    O: '#FF5800',
};

function renderCube(cube) {
    ['U','L','F','R','B','D'].forEach(faceKey => {
        const faceEl = document.getElementById(faceKey);
        faceEl.innerHTML = '';

        cube[faceKey].forEach(row => {
            row.forEach(color => {
                const s = document.createElement('div');
                s.className = 'sticker';
                s.style.background = colorMap[color];
                faceEl.appendChild(s);
            });
        });
    });
}

renderCube(applyScramble(scramble));
