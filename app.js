// Gothic 1 Remake Lockpick Solver - Application Logic

const DONATE_BNB = "0x6458D300b0f3e64BdD2DF92F5e258D735519bC67";
const DONATE_ETH = "0x6458D300b0f3e64BdD2DF92F5e258D735519bC67";
const DONATE_SOL = "7ADMFTViAtKPTszkuFGos3c1kwyB6hbYHiQBW837AkXJ";
const DONATE_TON = "UQAx2FG1NO6ifxOgbsp3Dqm6Fu325mZwlqKdOvAnHo77fVVo";

const TRANSLATIONS = {
    "RU": {
        "title": "Gothic 1 Remake Lockpick Solver by Ainez",
        "plate_short": "П{}",
        "hdr_title": "⚔  GOTHIC — РЕШАТЕЛЬ ЗАМКОВ  ⚔",
        "rules_btn": "⚙  Правила",
        "legend_title": "ПЛАСТИНЫ ЗАМКА",
        "not_zero": "не в нуле",
        "at_zero": "в нуле (цель)",
        "solve_btn": "🔓  НАЙТИ РЕШЕНИЕ",
        "solve_searching": "⏳  Поиск...",
        "reset_btn": "↺  Сброс",
        "status_init": "Установи начальное положение и нажми «Найти решение»",
        "status_reset": "Сброс выполнен. Задайте положения и правила нового замка",
        "status_changed": "Положение изменено. Нажмите «Найти решение»",
        "status_no_solution": "❌ Решение не найдено",
        "status_already_solved": "✅ Все пластины уже в нуле!",
        "status_solved": "✅ Найдено: {} ходов",
        "status_rules_saved": "Правила замка сохранены. Нажмите «Найти решение»",
        "steps_header": "ХОДЫ",
        "step_plate": "Пластина",
        "step_left": "◀ влево",
        "step_right": "▶ вправо",
        "pb_prev": "◀ пред",
        "pb_next": "след ▶",
        "pb_step": "шаг {}/{}",
        "rw_title": "Правила замка",
        "rw_header": "РЕДАКТОР ПРАВИЛ",
        "rw_subtitle": "Какие пластины двигаются при ходе ВЛЕВО (помимо самой пластины)",
        "rw_plate_left": "П{} влево →",
        "rw_moves": "двигает П",
        "rw_left": "влево",
        "rw_right": "вправо",
        "rw_save": "СОХРАНИТЬ",
        "support_btn": "💖 Поддержать автора",
        "sup_title": "Поддержка автора",
        "sup_header": "ПОДДЕРЖКА АВТОРА",
        "sup_desc": "Привет! Я Ainez. Этот решатель создавался для себя, чтобы сделать взлом в Готике и Ремейке максимально удобным и комфортным, и выложен в свободный доступ. Если у вас есть желание и возможность отблагодарить за работу — буду очень рад поддержке!\n\nС любовью, Ainez 💖",
        "sup_copy": "Копировать",
        "sup_copied": "Скопировано!",
        "topmost_opts": ["Обычное", "Поверх"]
    },
    "EN": {
        "title": "Gothic 1 Remake Lockpick Solver by Ainez",
        "plate_short": "P{}",
        "hdr_title": "⚔  GOTHIC — LOCKPICK SOLVER  ⚔",
        "rules_btn": "⚙  Rules",
        "legend_title": "LOCK PLATES",
        "not_zero": "not at zero",
        "at_zero": "at zero (goal)",
        "solve_btn": "🔓  FIND SOLUTION",
        "solve_searching": "⏳  Searching...",
        "reset_btn": "↺  Reset",
        "status_init": "Set initial state and click \"Find Solution\"",
        "status_reset": "Reset complete. Set positions and rules of the new lock",
        "status_changed": "Position changed. Click \"Find Solution\"",
        "status_no_solution": "❌ Solution not found",
        "status_already_solved": "✅ All plates are already at zero!",
        "status_solved": "✅ Found: {} steps",
        "status_rules_saved": "Lock rules saved. Click \"Find Solution\"",
        "steps_header": "STEPS",
        "step_plate": "Plate",
        "step_left": "◀ left",
        "step_right": "▶ right",
        "pb_prev": "◀ prev",
        "pb_next": "next ▶",
        "pb_step": "step {}/{}",
        "rw_title": "Lock Rules",
        "rw_header": "RULES EDITOR",
        "rw_subtitle": "Which plates move when shifting LEFT (in addition to the plate itself)",
        "rw_plate_left": "P{} left →",
        "rw_moves": "moves P",
        "rw_left": "left",
        "rw_right": "right",
        "rw_save": "SAVE",
        "support_btn": "💖 Support the Author",
        "sup_title": "Support the Author",
        "sup_header": "SUPPORT THE AUTHOR",
        "sup_desc": "Hi! I'm Ainez. This solver was created for personal use to make lockpicking in Gothic and the Remake as convenient and comfortable as possible, and is released for free. If you have the desire and ability to thank the author for their work — any support is highly appreciated!\n\nWith love, Ainez 💖",
        "sup_copy": "Copy",
        "sup_copied": "Copied!",
        "topmost_opts": ["Normal", "On Top"]
    }
};

// Application State
let state = {
    lang: "EN",
    n_plates: 6,
    positions: [0, 0, 0, 0, 0, 0],
    // Default rules: each plate moves itself left/right
    rules: [
        [[0, 1]],
        [[1, 1]],
        [[2, 1]],
        [[3, 1]],
        [[4, 1]],
        [[5, 1]]
    ],
    solution: [], // Array of { plate, direction }
    pb_states: [], // Playback position states
    pb_idx: -1 // Current playback step index
};

// Canvas drawing constants (matching Tkinter version)
const PLATE_W = 440;
const PLATE_H = 44;
const HOLE_R = 10;
const HOLE_GAP = 6;
const PIN_R = 6;
const PANEL2_COLOR = "#231f18";
const BORDER_COLOR = "#3a3020";
const HOLE_BG_COLOR = "#0e0c09";
const HOLE_RING_COLOR = "#2a2418";
const HOLE_CTR_COLOR = "#4a3a22";
const RED_PIN_COLOR = "#c0392b";
const YELLOW_PIN_COLOR = "#c8940a";
const RED_GLOW_COLOR = "#8b1a14";
const YELLOW_GLOW_COLOR = "#7a5a08";

// Initialization
window.onload = function() {
    buildPlatesUI();
    buildRulesUI();
    changeLang("EN");
    bindEvents();
    
    // Draw initial state for all plates
    for (let i = 0; i < state.n_plates; i++) {
        drawPlate(i);
    }
};

// Build plate rows in HTML
function buildPlatesUI() {
    const list = getEl("plates-list");
    list.innerHTML = "";
    
    // Build rows from 5 down to 0 (top to bottom layout)
    for (let i = state.n_plates - 1; i >= 0; i--) {
        const row = list.ownerDocument.createElement("div");
        row.className = "plate-row";
        
        const label = list.ownerDocument.createElement("div");
        label.className = "plate-lbl";
        label.id = `plate-lbl-${i}`;
        label.textContent = `P${i+1}`;
        row.appendChild(label);
        
        const canvasWrapper = list.ownerDocument.createElement("div");
        canvasWrapper.className = "canvas-wrapper";
        
        const canvas = list.ownerDocument.createElement("canvas");
        canvas.id = `canvas-${i}`;
        canvas.className = "plate-canvas";
        canvas.width = PLATE_W;
        canvas.height = PLATE_H;
        canvasWrapper.appendChild(canvas);
        row.appendChild(canvasWrapper);
        
        const ctrls = list.ownerDocument.createElement("div");
        ctrls.className = "plate-ctrls";
        
        const leftBtn = list.ownerDocument.createElement("button");
        leftBtn.className = "arrow-btn";
        leftBtn.textContent = "◀";
        leftBtn.addEventListener("click", () => adjustPlate(i, 1));
        ctrls.appendChild(leftBtn);
        
        const valLbl = list.ownerDocument.createElement("span");
        valLbl.id = `val-lbl-${i}`;
        valLbl.className = "val-lbl red";
        valLbl.textContent = "0";
        ctrls.appendChild(valLbl);
        
        const rightBtn = list.ownerDocument.createElement("button");
        rightBtn.className = "arrow-btn";
        rightBtn.textContent = "▶";
        rightBtn.addEventListener("click", () => adjustPlate(i, -1));
        ctrls.appendChild(rightBtn);
        
        row.appendChild(ctrls);
        list.appendChild(row);
    }
}

// Draw a single plate on its canvas
function drawPlate(idx) {
    const canvas = getEl(`canvas-${idx}`);
    if (!canvas) return;
    const ctx = canvas.getContext("2d");
    
    const value = state.positions[idx];
    const step = HOLE_R * 2 + HOLE_GAP; // 26px per step
    const center_x = PLATE_W / 2;
    const cy = PLATE_H / 2;
    const plate_w = 240;
    const plate_half_w = plate_w / 2;
    const offset = -value * step;

    // 1. Clear background
    ctx.fillStyle = HOLE_BG_COLOR;
    ctx.fillRect(0, 0, PLATE_W, PLATE_H);

    // 2. Draw sliding plate
    const px1 = center_x - plate_half_w + offset;
    const px2 = center_x + plate_half_w + offset;
    
    ctx.fillStyle = PANEL2_COLOR;
    ctx.fillRect(px1, 2, plate_w, PLATE_H - 4);
    
    ctx.lineWidth = 1;
    ctx.strokeStyle = BORDER_COLOR;
    ctx.strokeRect(px1, 2, plate_w, PLATE_H - 4);

    // 3. Draw sliding holes
    for (let pos = -3; pos <= 3; pos++) {
        const cx = center_x + pos * step + offset;
        // Verify hole fits inside the visual plate boundaries
        if (cx < px1 + HOLE_R || cx > px2 - HOLE_R) {
            continue;
        }
        
        const isTarget = (pos === 0);
        ctx.beginPath();
        ctx.arc(cx, cy, HOLE_R, 0, 2 * Math.PI);
        ctx.fillStyle = HOLE_BG_COLOR;
        ctx.fill();
        ctx.lineWidth = isTarget ? 2 : 1;
        ctx.strokeStyle = isTarget ? HOLE_CTR_COLOR : HOLE_RING_COLOR;
        ctx.stroke();
    }

    // 4. Draw static centered glowing pin
    const isAtZero = (value === 0);
    const pinCol = isAtZero ? RED_PIN_COLOR : YELLOW_PIN_COLOR;
    const glowCol = isAtZero ? RED_GLOW_COLOR : YELLOW_GLOW_COLOR;

    // Draw outer glow ring
    ctx.beginPath();
    ctx.arc(center_x, cy, PIN_R + 2, 0, 2 * Math.PI);
    ctx.lineWidth = 1;
    ctx.strokeStyle = glowCol;
    ctx.stroke();

    // Draw solid inner pin
    ctx.beginPath();
    ctx.arc(center_x, cy, PIN_R, 0, 2 * Math.PI);
    ctx.fillStyle = pinCol;
    ctx.fill();
}

// Adjust plate offset value
function adjustPlate(idx, delta) {
    let newVal = state.positions[idx] + delta;
    if (newVal < -3 || newVal > 3) return;
    
    state.positions[idx] = newVal;
    drawPlate(idx);
    updateValLabel(idx);
    clearSolution();
}

// Update numerical label adjacent to arrows
function updateValLabel(idx) {
    const lbl = getEl(`val-lbl-${idx}`);
    if (!lbl) return;
    const val = state.positions[idx];
    
    lbl.textContent = val > 0 ? `+${val}` : `${val}`;
    if (val === 0) {
        lbl.className = "val-lbl red";
    } else {
        lbl.className = "val-lbl yellow";
    }
}

// Handle UI translation switches
function changeLang(newLang) {
    state.lang = newLang;
    
    // Toggle active classes on lang buttons
    getEl("lang-en").className = newLang === "EN" ? "lang-opt active" : "lang-opt";
    getEl("lang-ru").className = newLang === "RU" ? "lang-opt active" : "lang-opt";
    
    const t = TRANSLATIONS[newLang];
    
    // Header & Title
    document.title = t["title"];
    getEl("hdr-title").textContent = t["hdr_title"];
    getEl("rules-btn").textContent = t["rules_btn"];
    
    // Always on Top Switcher labels
    getEl("topmost-normal").textContent = t["topmost_opts"][0];
    getEl("topmost-on").textContent = t["topmost_opts"][1];
    
    // Legend
    getEl("legend-title").textContent = t["legend_title"];
    getEl("txt-not-zero").textContent = t["not_zero"];
    getEl("txt-at-zero").textContent = t["at_zero"];
    
    // Solver Main Actions
    getEl("solve-btn").textContent = t["solve_btn"];
    getEl("reset-btn").textContent = t["reset_btn"];
    
    // Playback Controls
    getEl("pb-prev").textContent = t["pb_prev"];
    getEl("pb-next").textContent = t["pb_next"];
    
    // Steps Frame Header
    getEl("steps-header").textContent = t["steps_header"];
    
    // Support Modal & Buttons
    getEl("support-btn").textContent = t["support_btn"];
    getEl("sup-title").textContent = t["sup_title"];
    getEl("sup-header").textContent = t["sup_header"];
    getEl("sup-desc").textContent = t["sup_desc"];
    getEl("sup-footer").textContent = newLang === "RU" ? "С любовью, Ainez 💖" : "With love, Ainez 💖";
    
    // Support Modal Copy Buttons
    ["bnb", "eth", "sol", "ton"].forEach(id => {
        const btn = getEl(`copy-${id}`);
        if (btn && !btn.classList.contains("copied")) {
            btn.textContent = t["sup_copy"];
        }
    });
    
    // Rules Modal Titles
    getEl("rw-title").textContent = t["rw_title"];
    getEl("rw-header").textContent = t["rw_header"];
    getEl("rw-subtitle").textContent = t["rw_subtitle"];
    getEl("rw-save").textContent = t["rw_save"];
    
    // Plate short labels P1/П1
    for (let i = 0; i < state.n_plates; i++) {
        getEl(`plate-lbl-${i}`).textContent = t["plate_short"].replace("{}", i+1);
    }
    
    // Re-translate status label & modal rules
    updateStatusText();
    buildRulesUI();
    
    // Re-render solution steps if they exist
    if (state.solution.length > 0) {
        renderStepsList();
        updatePlaybackLabel();
    }
}

// Reset all values back to target zero
function resetPositions() {
    state.positions = [0, 0, 0, 0, 0, 0];
    state.rules = [
        [[0, 1]],
        [[1, 1]],
        [[2, 1]],
        [[3, 1]],
        [[4, 1]],
        [[5, 1]]
    ];
    
    // Redraw
    for (let i = 0; i < state.n_plates; i++) {
        drawPlate(i);
        updateValLabel(i);
    }
    
    clearSolution();
    buildRulesUI(); // reset rules visual checks
    
    const t = TRANSLATIONS[state.lang];
    getEl("status-lbl").textContent = t["status_reset"];
    getEl("status-lbl").style.color = "var(--gold-color)";
}

// Clean solution list when values shift
function clearSolution() {
    state.solution = [];
    state.pb_states = [];
    state.pb_idx = -1;
    
    getEl("steps-scroll").innerHTML = "";
    updateStatusText();
    updatePlaybackLabel();
    updatePlaybackBtns();
}

// Update status text based on state variables
function updateStatusText() {
    const t = TRANSLATIONS[state.lang];
    const lbl = getEl("status-lbl");
    lbl.style.color = "var(--muted-color)";
    
    // Default initial text
    if (state.positions.every(v => v === 0) && state.solution.length === 0) {
        lbl.textContent = t["status_init"];
        return;
    }
    
    if (state.solution.length === 0) {
        lbl.textContent = t["status_changed"];
    } else {
        lbl.textContent = t["status_solved"].replace("{}", state.solution.length);
        lbl.style.color = "var(--gold-color)";
    }
}

// Add dynamic effect row to the container in Rules Editor
function addEffectRow(container, plateIdx, targetPlateIdx, direction) {
    const row = container.ownerDocument.createElement("div");
    row.className = "effect-row";
    
    const t = TRANSLATIONS[state.lang];
    
    const movesLabel = container.ownerDocument.createElement("span");
    movesLabel.className = "effect-moves-lbl";
    movesLabel.textContent = t["rw_moves"];
    row.appendChild(movesLabel);
    
    // Exclude self-plate from target options
    const targetSelect = container.ownerDocument.createElement("select");
    targetSelect.className = "effect-plate-sel";
    for (let j = 0; j < state.n_plates; j++) {
        if (j === plateIdx) continue;
        const opt = container.ownerDocument.createElement("option");
        opt.value = j;
        opt.textContent = j + 1;
        if (j === targetPlateIdx) opt.selected = true;
        targetSelect.appendChild(opt);
    }
    row.appendChild(targetSelect);
    
    const dirSelect = container.ownerDocument.createElement("select");
    dirSelect.className = "effect-dir-sel";
    const dirLeftOpt = container.ownerDocument.createElement("option");
    dirLeftOpt.value = "1";
    dirLeftOpt.textContent = t["rw_left"];
    if (direction === 1) dirLeftOpt.selected = true;
    dirSelect.appendChild(dirLeftOpt);
    
    const dirRightOpt = container.ownerDocument.createElement("option");
    dirRightOpt.value = "-1";
    dirRightOpt.textContent = t["rw_right"];
    if (direction === -1) dirRightOpt.selected = true;
    dirSelect.appendChild(dirRightOpt);
    
    row.appendChild(dirSelect);
    
    const deleteBtn = container.ownerDocument.createElement("button");
    deleteBtn.className = "effect-delete-btn";
    deleteBtn.textContent = "✕";
    deleteBtn.addEventListener("click", () => {
        row.remove();
    });
    row.appendChild(deleteBtn);
    
    container.appendChild(row);
}

// Rules Modal builder
function buildRulesUI() {
    const grid = getEl("rules-grid");
    grid.innerHTML = "";
    
    const t = TRANSLATIONS[state.lang];
    
    for (let i = 0; i < state.n_plates; i++) {
        const row = grid.ownerDocument.createElement("div");
        row.className = "rules-row";
        
        const label = grid.ownerDocument.createElement("div");
        label.className = "rules-row-lbl";
        label.textContent = t["rw_plate_left"].replace("{}", i+1);
        row.appendChild(label);
        
        const effectsContainer = grid.ownerDocument.createElement("div");
        effectsContainer.className = "rules-effects-container";
        effectsContainer.id = `effects-container-${i}`;
        row.appendChild(effectsContainer);
        
        // Populating existing rules (excluding self)
        state.rules[i].forEach(dep => {
            const target = dep[0];
            const dir = dep[1];
            if (target !== i) {
                addEffectRow(effectsContainer, i, target, dir);
            }
        });
        
        const addBtn = grid.ownerDocument.createElement("button");
        addBtn.className = "add-effect-btn";
        addBtn.textContent = "+";
        addBtn.addEventListener("click", () => {
            // Default target plate is the first available plate
            const defaultTarget = (i === 0) ? 1 : 0;
            addEffectRow(effectsContainer, i, defaultTarget, 1);
        });
        row.appendChild(addBtn);
        
        grid.appendChild(row);
        
        // Separator line
        if (i < state.n_plates - 1) {
            const sep = grid.ownerDocument.createElement("div");
            sep.className = "rules-separator";
            grid.appendChild(sep);
        }
    }
}

// Modal Toggle Handlers
function openRules() {
    buildRulesUI();
    getEl("rules-modal").classList.add("open");
}

function closeRules() {
    getEl("rules-modal").classList.remove("open");
}

function saveRules() {
    // Save rules state from dynamic modal controls
    for (let i = 0; i < state.n_plates; i++) {
        // Start with self-movement rule
        const newRule = [[i, 1]];
        
        const container = getEl(`effects-container-${i}`);
        if (container) {
            const rows = container.getElementsByClassName("effect-row");
            for (let r = 0; r < rows.length; r++) {
                const plateSel = rows[r].getElementsByClassName("effect-plate-sel")[0];
                const dirSel = rows[r].getElementsByClassName("effect-dir-sel")[0];
                if (plateSel && dirSel) {
                    const target = parseInt(plateSel.value);
                    const dir = parseInt(dirSel.value);
                    newRule.push([target, dir]);
                }
            }
        }
        state.rules[i] = newRule;
    }
    
    closeRules();
    clearSolution();
    
    const t = TRANSLATIONS[state.lang];
    const lbl = getEl("status-lbl");
    lbl.textContent = t["status_rules_saved"];
    lbl.style.color = "var(--gold-color)";
}

function openSupport() {
    getEl("support-modal").classList.add("open");
}

function closeSupport() {
    getEl("support-modal").classList.remove("open");
}

// Copy to Clipboard helper
function copyCrypto(id, text) {
    navigator.clipboard.writeText(text).then(() => {
        const btn = getEl(`copy-${id}`);
        const t = TRANSLATIONS[state.lang];
        if (btn) {
            btn.textContent = t["sup_copied"];
            btn.classList.add("copied");
            
            setTimeout(() => {
                btn.textContent = t["sup_copy"];
                btn.classList.remove("copied");
            }, 1500);
        }
    }).catch(err => {
        console.error("Failed to copy text: ", err);
    });
}

// Optimal Solver computation
function solveLock() {
    const t = TRANSLATIONS[state.lang];
    const lbl = getEl("status-lbl");
    
    // 1. If already at target goal state
    if (state.positions.every(v => v === 0)) {
        lbl.textContent = t["status_already_solved"];
        lbl.style.color = "var(--gold-color)";
        return;
    }
    
    lbl.textContent = t["solve_searching"];
    
    // Run solver in next frame to prevent frame freezes during calculation
    setTimeout(() => {
        const path = bfs(state.positions, state.n_plates, state.rules);
        
        if (path === null) {
            lbl.textContent = t["status_no_solution"];
            lbl.style.color = "#8a3030";
            return;
        }
        
        state.solution = path;
        
        // Build playback positions sequence
        let curState = [...state.positions];
        state.pb_states = [[...curState]];
        path.forEach(step => {
            curState = applyMove(curState, step.plate, step.direction, state.rules);
            state.pb_states.push([...curState]);
        });
        
        state.pb_idx = 0; // set index to start step
        
        renderStepsList();
        updateStatusText();
        updatePlaybackLabel();
        updatePlaybackBtns();
        highlightActiveStep(0);
    }, 50);
}

// Render computed moves list in DOM
function renderStepsList() {
    const container = getEl("steps-scroll");
    container.innerHTML = "";
    
    const t = TRANSLATIONS[state.lang];
    
    state.solution.forEach((step, idx) => {
        const item = container.ownerDocument.createElement("div");
        item.className = "step-item";
        item.id = `step-item-${idx}`;
        item.addEventListener("click", () => jumpToStep(idx));
        
        const nxt = state.pb_states[idx + 1];
        const stateStr = nxt.map(v => v > 0 ? `+${v}` : `${v}`).join("  ");
        
        const isLeft = (step.direction === 1);
        const dirTxt = isLeft ? t["step_left"] : t["step_right"];
        const dirClass = isLeft ? "step-left" : "step-right";
        
        item.innerHTML = `
            <div class="step-col step-num">${idx + 1}.</div>
            <div class="step-col step-plate-name">${t["step_plate"]} ${step.plate + 1}</div>
            <div class="step-col step-dir ${dirClass}">${dirTxt}</div>
            <div class="step-col step-state">[${stateStr}]</div>
        `;
        container.appendChild(item);
    });
}

// BFS Solver Functions
function applyMove(state, plateIdx, direction, rules) {
    let s = [...state];
    let rule = rules[plateIdx];
    for (let i = 0; i < rule.length; i++) {
        let p = rule[i][0];
        let d = rule[i][1];
        let new_val = s[p] + d * direction;
        if (new_val > 3 || new_val < -3) {
            return null; // invalid move out of lock bounds
        }
        s[p] = new_val;
    }
    return s;
}

function bfs(start, n, rules, max_iter = 500000) {
    let goal = Array(n).fill(0);
    if (start.every((v, i) => v === goal[i])) return [];
    
    let q = [start];
    let q_head = 0;
    let vis = {};
    vis[start.toString()] = null;
    let found = null;
    let iters = 0;
    
    while (q_head < q.length && iters < max_iter) {
        iters++;
        let cur = q[q_head++];
        
        for (let p = 0; p < n; p++) {
            for (let d of [1, -1]) {
                let nxt = applyMove(cur, p, d, rules);
                if (nxt === null) continue;
                let nxtKey = nxt.toString();
                if (!(nxtKey in vis)) {
                    vis[nxtKey] = { prev: cur, plate: p, direction: d };
                    if (nxt.every((v, i) => v === 0)) {
                        found = nxt;
                        break;
                    }
                    q.push(nxt);
                }
            }
            if (found) break;
        }
        if (found) break;
    }
    
    if (!found) return null;
    
    let path = [];
    let cur = found;
    while (vis[cur.toString()]) {
        let step = vis[cur.toString()];
        path.push({ plate: step.plate, direction: step.direction });
        cur = step.prev;
    }
    path.reverse();
    return path;
}

// Playback Visual Stepper Controls
function updatePlaybackLabel() {
    const lbl = getEl("pb-lbl");
    const t = TRANSLATIONS[state.lang];
    if (state.solution.length === 0) {
        lbl.textContent = t["pb_step"].replace("{}", 0).replace("{}", 0);
    } else {
        lbl.textContent = t["pb_step"].replace("{}", state.pb_idx).replace("{}", state.solution.length);
    }
}

function updatePlaybackBtns() {
    const len = state.solution.length;
    const hasSol = len > 0;
    
    getEl("pb-prev").disabled = !hasSol || state.pb_idx <= 0;
    getEl("pb-next").disabled = !hasSol || state.pb_idx >= len;
    getEl("pb-rst").disabled = !hasSol;
}

function setPlaybackState(idx) {
    state.pb_idx = idx;
    
    // Apply position frame
    state.positions = [...state.pb_states[idx]];
    
    // Redraw all canvases to show active sliding positions
    for (let i = 0; i < state.n_plates; i++) {
        drawPlate(i);
        updateValLabel(i);
    }
    
    updatePlaybackLabel();
    updatePlaybackBtns();
    highlightActiveStep(idx);
}

function highlightActiveStep(idx) {
    // Clear previous highlights
    for (let i = 0; i < state.solution.length; i++) {
        const item = getEl(`step-item-${i}`);
        if (item) {
            item.className = "step-item";
        }
    }
    
    // Highlight step item corresponding to the next move to make (idx)
    // When idx == solution.length, all moves are completed (no next move)
    if (idx < state.solution.length) {
        const activeItem = getEl(`step-item-${idx}`);
        if (activeItem) {
            activeItem.className = "step-item active";
            
            // Auto scroll container to keep active step visible
            activeItem.scrollIntoView({ behavior: 'smooth', block: 'nearest' });
        }
    }
}

function playbackPrev() {
    if (state.pb_idx > 0) {
        setPlaybackState(state.pb_idx - 1);
    }
}

function playbackNext() {
    if (state.pb_idx < state.solution.length) {
        setPlaybackState(state.pb_idx + 1);
    }
}

function playbackReset() {
    setPlaybackState(0);
}

function jumpToStep(idx) {
    setPlaybackState(idx);
}

async function setTopmost(enable) {
    state.topmost = enable;
    
    // Toggle active class on topmost buttons
    getEl("topmost-normal").className = enable ? "topmost-opt" : "topmost-opt active";
    getEl("topmost-on").className = enable ? "topmost-opt active" : "topmost-opt";
    
    if (enable) {
        // Try Picture-in-Picture
        if ('documentPictureInPicture' in window) {
            try {
                await startPiP();
            } catch (err) {
                console.error("PiP error:", err);
                showNotification(state.lang === "RU" ? "Не удалось открыть поверх. Используйте расширение браузера." : "Failed to open topmost. Use a browser extension.");
                // Reset visual state
                getEl("topmost-normal").className = "topmost-opt active";
                getEl("topmost-on").className = "topmost-opt";
                state.topmost = false;
            }
        } else {
            showNotification(state.lang === "RU" ? "Браузер не поддерживает режим 'Поверх'. Рекомендуется использовать Chrome/Edge." : "Browser doesn't support 'Always on Top' mode. Recommended to use Chrome/Edge.");
            // Reset visual state
            getEl("topmost-normal").className = "topmost-opt active";
            getEl("topmost-on").className = "topmost-opt";
            state.topmost = false;
        }
    } else {
        if (window.pipWindow) {
            window.pipWindow.close();
        }
    }
}

async function startPiP() {
    if (window.pipWindow) {
        window.pipWindow.close();
        return;
    }
    
    const container = document.querySelector('.app-container');
    const width = container.offsetWidth || 680;
    const height = container.offsetHeight || 720;
    
    const pipWindow = await documentPictureInPicture.requestWindow({
        width: width,
        height: height
    });
    
    window.pipWindow = pipWindow;
    
    // Copy stylesheets
    [...document.styleSheets].forEach((styleSheet) => {
        try {
            const cssRules = [...styleSheet.cssRules].map((rule) => rule.cssText).join('');
            const style = pipWindow.document.createElement('style');
            style.textContent = cssRules;
            pipWindow.document.head.appendChild(style);
        } catch (e) {
            const link = pipWindow.document.createElement('link');
            link.rel = 'stylesheet';
            link.type = styleSheet.type || 'text/css';
            link.href = styleSheet.href;
            pipWindow.document.head.appendChild(link);
        }
    });
    
    // Copy font links or other header elements
    [...document.querySelectorAll('link[rel="preconnect"], link[href*="fonts.googleapis.com"]')].forEach(link => {
        pipWindow.document.head.appendChild(link.cloneNode(true));
    });
    
    // Move container
    pipWindow.document.body.appendChild(container);
    
    // Listen for close to restore container
    pipWindow.addEventListener("pagehide", () => {
        document.body.appendChild(container);
        window.pipWindow = null;
        setTopmost(false);
    });
}

function showNotification(msg) {
    const statusLbl = getEl("status-lbl");
    const oldText = statusLbl.textContent;
    const oldColor = statusLbl.style.color;
    
    statusLbl.textContent = msg;
    statusLbl.style.color = "var(--gold-color)";
    
    setTimeout(() => {
        if (statusLbl.textContent === msg) {
            statusLbl.textContent = oldText;
            statusLbl.style.color = oldColor;
        }
    }, 4000);
}


// Helper function to query elements from either main document or PiP document context
function getEl(id) {
    if (window.pipWindow && window.pipWindow.document) {
        const el = window.pipWindow.document.getElementById(id);
        if (el) return el;
    }
    return document.getElementById(id);
}


// Helper to bind all static DOM event listeners programmatically (cross-document safe)
function bindEvents() {
    // Topmost switcher
    getEl("topmost-normal").addEventListener("click", () => setTopmost(false));
    getEl("topmost-on").addEventListener("click", () => setTopmost(true));
    
    // Language switcher
    getEl("lang-en").addEventListener("click", () => changeLang("EN"));
    getEl("lang-ru").addEventListener("click", () => changeLang("RU"));
    
    // Header controls
    getEl("rules-btn").addEventListener("click", openRules);
    
    // Solver actions
    getEl("solve-btn").addEventListener("click", solveLock);
    getEl("reset-btn").addEventListener("click", resetPositions);
    
    // Playback controls
    getEl("pb-prev").addEventListener("click", playbackPrev);
    getEl("pb-next").addEventListener("click", playbackNext);
    getEl("pb-rst").addEventListener("click", playbackReset);
    
    // Support button
    getEl("support-btn").addEventListener("click", openSupport);
    
    // Rules Modal actions
    const rulesCloseBtn = getEl("rules-modal").querySelector(".close-btn");
    if (rulesCloseBtn) rulesCloseBtn.addEventListener("click", closeRules);
    getEl("rw-save").addEventListener("click", saveRules);
    
    // Support Modal actions
    const supportCloseBtn = getEl("support-modal").querySelector(".close-btn");
    if (supportCloseBtn) supportCloseBtn.addEventListener("click", closeSupport);
    
    // Support Modal copy buttons
    getEl("copy-bnb").addEventListener("click", () => copyCrypto('bnb', DONATE_BNB));
    getEl("copy-eth").addEventListener("click", () => copyCrypto('eth', DONATE_ETH));
    getEl("copy-sol").addEventListener("click", () => copyCrypto('sol', DONATE_SOL));
    getEl("copy-ton").addEventListener("click", () => copyCrypto('ton', DONATE_TON));
}
