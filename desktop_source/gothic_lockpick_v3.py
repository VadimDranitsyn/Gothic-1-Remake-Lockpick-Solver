import customtkinter as ctk
import tkinter as tk
import tkinter.ttk as ttk
import ctypes
from collections import deque


def _apply_dark_titlebar(window):
    """Форсирует тёмный заголовок окна на Windows через DWM API."""
    try:
        DWMWA_USE_IMMERSIVE_DARK_MODE = 20
        GA_ROOT = 2
        hwnd = window.winfo_id()
        # GetAncestor(GA_ROOT) — надёжно находит корневое окно с тайтлбаром
        root_hwnd = ctypes.windll.user32.GetAncestor(hwnd, GA_ROOT)
        if root_hwnd:
            hwnd = root_hwnd
        value = ctypes.c_int(1)
        ctypes.windll.dwmapi.DwmSetWindowAttribute(
            hwnd, DWMWA_USE_IMMERSIVE_DARK_MODE,
            ctypes.byref(value), ctypes.sizeof(value))
    except Exception:
        pass  # не Windows или старая версия — молча игнорируем

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("dark-blue")

# Donation Details / Реквизиты для поддержки автора
DONATE_BNB  = "0x6458D300b0f3e64BdD2DF92F5e258D735519bC67"
DONATE_ETH  = "0x6458D300b0f3e64BdD2DF92F5e258D735519bC67"
DONATE_SOL  = "7ADMFTViAtKPTszkuFGos3c1kwyB6hbYHiQBW837AkXJ"
DONATE_TON  = "UQAx2FG1NO6ifxOgbsp3Dqm6Fu325mZwlqKdOvAnHo77fVVo"

BG         = "#13110e"
PANEL      = "#1c1810"
PANEL2     = "#231f18"
BORDER     = "#3a3020"
GOLD       = "#c8a84b"
GOLD2      = "#e8c86a"
RED_PIN    = "#c0392b"
YELLOW_PIN = "#c8940a"
HOLE_BG    = "#0e0c09"
HOLE_RING  = "#2a2418"
HOLE_CTR   = "#4a3a22"
MUTED      = "#6a5a3a"
TEXT       = "#d4c9a8"
BTN        = "#1a1610"
BTN_HOV    = "#2a2418"
BLUE_DIR   = "#5a9fd4"
RED_DIR    = "#c0502b"
RED_MUTED  = "#5c2020"   # пастельный красный для кнопки сброса
RED_MUTED2 = "#7a2a2a"   # hover

HOLE_R   = 10
HOLE_GAP = 6
PIN_R    = 6
N_HOLES  = 7

TRANSLATIONS = {
    "RU": {
        "title": "Gothic 1 Remake Lockpick Solver by Ainez",
        "plate_short": "П{}",
        "hdr_title": "⚔  GOTHIC — РЕШАТЕЛЬ ЗАМКОВ  ⚔",
        "rules_btn": "⚙  Правила",
        "topmost_btn": "📌  Поверх",
        "topmost_btn_on": "📌  Поверх ВКЛ",
        "legend_title": "ПЛАСТИНЫ ЗАМКА",
        "not_zero": "не в нуле",
        "at_zero": "в нуле (цель)",
        "solve_btn": "🔓  НАЙТИ РЕШЕНИЕ",
        "solve_searching": "⏳  Поиск...",
        "reset_btn": "↺  Сброс",
        "status_init": "Установи начальное положение и нажми «Найти решение»",
        "status_reset": "Сброс выполнен. Задай положения и правила нового замка",
        "status_changed": "Положение изменено. Нажми «Найти решение»",
        "status_no_solution": "❌ Решение не найдено",
        "status_already_solved": "✅ Все пластины уже в нуле!",
        "status_solved": "✅ Найдено: {} ходов",
        "status_rules_saved": "Правила замка сохранены. Нажми «Найти решение»",
        "steps_header": "ХОДЫ",
        "step_plate": "Пластина",
        "step_left": "◀ влево",
        "step_right": "▶ вправо",
        "pb_prev": "◀ пред",
        "pb_next": "след ▶",
        "pb_step": "шаг {}/{}",
        "rw_title": "Правила замка",
        "rw_header": "РЕДАКТОР ПРАВИЛ",
        "rw_subtitle": "Какие пластины движутся при ходе ВЛЕВО (помимо самой пластины)",
        "rw_plate_left": "П{} влево →",
        "rw_moves": "двигает П",
        "rw_left": "влево",
        "rw_right": "вправо",
        "rw_save": "СОХРАНИТЬ",
        "topmost_opts": ["Обычное", "Поверх"],
        "support_btn": "💖 Поддержать автора",
        "sup_title": "Поддержка автора",
        "sup_header": "ПОДДЕРЖКА АВТОРА",
        "sup_desc": "Привет! Я Ainez. Этот решатель создавался для себя, чтобы сделать взлом в Готике и Ремейке максимально удобным и комфортным, и выложен в свободный доступ. Если у вас есть желание и возможность отблагодарить за работу — буду очень рад поддержке!\n\nС любовью, Ainez 💖",
        "sup_copy": "Копировать",
        "sup_copied": "Скопировано!",
    },
    "EN": {
        "title": "Gothic 1 Remake Lockpick Solver by Ainez",
        "plate_short": "P{}",
        "hdr_title": "⚔  GOTHIC — LOCKPICK SOLVER  ⚔",
        "rules_btn": "⚙  Rules",
        "topmost_btn": "📌  Always on Top",
        "topmost_btn_on": "📌  Always on Top ON",
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
        "topmost_opts": ["Normal", "On Top"],
        "support_btn": "💖 Support the Author",
        "sup_title": "Support the Author",
        "sup_header": "SUPPORT THE AUTHOR",
        "sup_desc": "Hi! I'm Ainez. This solver was created for personal use to make lockpicking in Gothic and the Remake as convenient and comfortable as possible, and is released for free. If you have the desire and ability to thank the author for their work — any support is highly appreciated!\n\nWith love, Ainez 💖",
        "sup_copy": "Copy",
        "sup_copied": "Copied!",
    }
}

def apply_move(state, plate_idx, direction, rules):
    s = list(state)
    for p, d in rules[plate_idx]:
        new_val = s[p] + d * direction
        if new_val > 3 or new_val < -3:
            return None
        s[p] = new_val
    return tuple(s)

def bfs(start, n, rules, max_iter=500000):
    goal = tuple([0]*n)
    if tuple(start) == goal: return []
    vis = {tuple(start): None}
    q = deque([tuple(start)])
    found = None
    iters = 0
    while q and iters < max_iter:
        iters += 1
        cur = q.popleft()
        for p in range(n):
            for d in [1, -1]:
                nxt = apply_move(cur, p, d, rules)
                if nxt is None: continue
                if nxt not in vis:
                    vis[nxt] = (cur, p, d)
                    if nxt == goal:
                        found = nxt
                        break
                    q.append(nxt)
            if found: break
        if found: break
    if not found: return None
    path = []
    cur = found
    while vis[cur]:
        prev, plate, direction = vis[cur]
        path.append((plate, direction))
        cur = prev
    path.reverse()
    return path


class PlateCanvas(tk.Canvas):
    PLATE_W = 440
    PLATE_H = 44

    def __init__(self, parent, idx, on_change, **kwargs):
        super().__init__(parent,
                         width=self.PLATE_W, height=self.PLATE_H,
                         bg=HOLE_BG, highlightthickness=0, **kwargs)
        self.idx = idx
        self.value = 0
        self.on_change = on_change
        self._draw()

    def _draw(self):
        self.delete("all")
        w, h = self.PLATE_W, self.PLATE_H
        step = HOLE_R * 2 + HOLE_GAP  # 26px на шаг
        center_x = w // 2             # пин всегда по центру канваса
        cy = h // 2
        plate_w = 240
        plate_half_w = plate_w // 2

        # Смещение пластины: при изменении значения пластина едет влево/вправо
        offset = -self.value * step

        # Рисуем саму скользящую пластину
        px1 = center_x - plate_half_w + offset
        px2 = center_x + plate_half_w + offset
        self.create_rectangle(px1, 2, px2, h-2, fill=PANEL2, outline=BORDER, width=1)

        # Рисуем отверстия, которые скользят вместе с пластиной
        for pos in range(-3, 4):
            cx = center_x + pos * step + offset
            # Рисуем только те отверстия, которые попадают на саму пластину
            if cx < px1 + HOLE_R or cx > px2 - HOLE_R:
                continue
            is_target = (pos == 0)  # целевое (нулевое) отверстие
            ring_col = HOLE_CTR if is_target else HOLE_RING
            ring_w   = 2 if is_target else 1
            self.create_oval(cx-HOLE_R, cy-HOLE_R, cx+HOLE_R, cy+HOLE_R,
                             fill=HOLE_BG, outline=ring_col, width=ring_w)

        # Пин неподвижен и всегда находится строго по центру
        pin_col  = RED_PIN    if self.value == 0 else YELLOW_PIN
        glow_col = "#8b1a14" if self.value == 0 else "#7a5a08"
        self.create_oval(center_x-PIN_R-2, cy-PIN_R-2,
                         center_x+PIN_R+2, cy+PIN_R+2,
                         fill="", outline=glow_col, width=1)
        self.create_oval(center_x-PIN_R, cy-PIN_R,
                         center_x+PIN_R, cy+PIN_R,
                         fill=pin_col, outline="")

    def set_value(self, v):
        self.value = v
        self._draw()

    def adjust(self, delta):
        new_val = self.value + delta
        if new_val < -3 or new_val > 3:
            return
        self.value = new_val
        self._draw()
        self.on_change()


class App(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.lang = "EN"
        self.title(TRANSLATIONS[self.lang]["title"])
        self.geometry("720x720")
        self.minsize(680, 670)
        self.configure(fg_color=BG)

        self.n_plates = 7
        self.positions = [0, 0, 0, 0, 0, 0, 0]
        self.rules = [
            [(0,1)],
            [(1,1)],
            [(2,1)],
            [(3,1)],
            [(4,1)],
            [(5,1)],
            [(6,1)],
        ]
        self.solution = []
        self.pb_states = []
        self.pb_idx = -1
        self.step_frames = []
        self._start_state = None

        self._build()
        # Тёмный заголовок окна на Windows
        self.after(100, lambda: _apply_dark_titlebar(self))

    def _build(self):
        # Тёмная тема для ttk.Combobox — один раз при старте
        _style = ttk.Style()
        _style.theme_use('clam')
        _style.configure('Dark.TCombobox',
            fieldbackground=BTN, background=BTN, foreground=TEXT,
            insertcolor=TEXT, selectbackground=BTN_HOV, selectforeground=TEXT,
            arrowcolor=GOLD, bordercolor=BORDER,
            lightcolor=BORDER, darkcolor=BORDER, troughcolor=BORDER)
        _style.map('Dark.TCombobox',
            fieldbackground=[
                ('readonly', '!disabled', BTN),
                ('!readonly', '!disabled', BTN),
                ('disabled', BORDER),
                ('', BTN),
            ],
            foreground=[
                ('readonly', TEXT), ('!readonly', TEXT),
                ('disabled', MUTED), ('', TEXT),
            ],
            background=[
                ('active', BTN_HOV), ('pressed', BTN_HOV),
                ('readonly', BTN), ('', BTN),
            ],
            selectbackground=[('readonly', BTN_HOV), ('', BTN_HOV)],
            selectforeground=[('readonly', TEXT), ('', TEXT)],
            arrowcolor=[('active', GOLD2), ('', GOLD)],
        )
        t = TRANSLATIONS[self.lang]

        # Header
        hdr = ctk.CTkFrame(self, fg_color=PANEL, corner_radius=0,
                            border_color=BORDER, border_width=1)
        hdr.pack(fill="x")

        self.hdr_title_lbl = ctk.CTkLabel(hdr, text=t["hdr_title"],
                     font=ctk.CTkFont(size=15, weight="bold"),
                     text_color=GOLD)
        self.hdr_title_lbl.pack(side="left", padx=18, pady=10)

        self.rules_btn = ctk.CTkButton(hdr, text=t["rules_btn"], width=120, height=30,
                      font=ctk.CTkFont(size=11, weight="bold"),
                      fg_color=GOLD, hover_color=GOLD2,
                      text_color=BG, corner_radius=5,
                      command=self._open_rules)
        self.rules_btn.pack(side="right", padx=(0,12), pady=8)

        # Language Switcher
        self.lang_btn = ctk.CTkSegmentedButton(
            hdr, values=["EN", "RU"], width=80, height=30,
            font=ctk.CTkFont(size=11, weight="bold"),
            fg_color=BORDER, selected_color=GOLD,
            selected_hover_color=GOLD2, unselected_color=BTN,
            unselected_hover_color=BTN_HOV, text_color=TEXT,
            border_width=1, corner_radius=5,
            command=self._on_lang_change
        )
        self.lang_btn.set(self.lang)
        self.lang_btn.pack(side="right", padx=(0,12), pady=8)

        # Always on Top Switcher
        self._topmost = False
        self.topmost_btn = ctk.CTkSegmentedButton(
            hdr, values=t["topmost_opts"], width=140, height=30,
            font=ctk.CTkFont(size=11, weight="bold"),
            fg_color=BORDER, selected_color=GOLD,
            selected_hover_color=GOLD2, unselected_color=BTN,
            unselected_hover_color=BTN_HOV, text_color=TEXT,
            border_width=1, corner_radius=5,
            command=self._on_topmost_change
        )
        self.topmost_btn.set(t["topmost_opts"][0])
        self.topmost_btn.pack(side="right", padx=(0,6), pady=8)

        # Apply initial text color contrast
        self.after(50, lambda: self._update_segmented_button_contrast(self.lang_btn))
        self.after(50, lambda: self._update_segmented_button_contrast(self.topmost_btn))

        # Lock visual area
        lock_outer = ctk.CTkFrame(self, fg_color=PANEL,
                                   border_color=BORDER, border_width=1, corner_radius=8)
        lock_outer.pack(fill="x", padx=14, pady=(12,4))

        # Legend
        leg_f = ctk.CTkFrame(lock_outer, fg_color="transparent")
        leg_f.pack(fill="x", padx=12, pady=(8,4))
        self.leg_title_lbl = ctk.CTkLabel(leg_f, text=t["legend_title"],
                     font=ctk.CTkFont(size=10, weight="bold"),
                     text_color=MUTED)
        self.leg_title_lbl.pack(side="left")

        self.leg_labels = []
        for col, txt_key in [(YELLOW_PIN, "not_zero"), (RED_PIN, "at_zero")]:
            f = ctk.CTkFrame(leg_f, fg_color="transparent")
            f.pack(side="right", padx=8)
            c = tk.Canvas(f, width=12, height=12, bg=PANEL, highlightthickness=0)
            c.pack(side="left", padx=(0,4))
            c.create_oval(1,1,11,11,fill=col,outline="")
            lbl = ctk.CTkLabel(f, text=t[txt_key], font=ctk.CTkFont(size=10), text_color=MUTED)
            lbl.pack(side="left")
            self.leg_labels.append((lbl, txt_key))

        plates_frame = ctk.CTkFrame(lock_outer, fg_color="#0e0c09",
                                     border_color=BORDER, border_width=1, corner_radius=6)
        plates_frame.pack(fill="x", padx=12, pady=(4,10))

        self.plate_canvases = [None] * self.n_plates
        self.row_labels = []
        for i in range(self.n_plates - 1, -1, -1):
            row = ctk.CTkFrame(plates_frame, fg_color="transparent")
            row.pack(fill="x", padx=8, pady=4)

            # Настраиваем grid для выравнивания:
            # col 0 (label) — слева, col 1 (canvas) — строго по центру, col 2 (controls) — справа
            row.columnconfigure(0, weight=1)
            row.columnconfigure(1, weight=0)
            row.columnconfigure(2, weight=1)

            lbl = ctk.CTkLabel(row, text=t["plate_short"].format(i+1),
                               font=ctk.CTkFont(size=11, weight="bold"),
                               text_color=MUTED, width=22)
            lbl.grid(row=0, column=0, sticky="w", padx=(8, 0))
            self.row_labels.append((lbl, i))

            pc = PlateCanvas(row, i, self._on_plate_change)
            pc.grid(row=0, column=1)
            pc.set_value(self.positions[i])
            self.plate_canvases[i] = pc

            ctrl = ctk.CTkFrame(row, fg_color="transparent")
            ctrl.grid(row=0, column=2, sticky="e", padx=(0, 8))

            ctk.CTkButton(ctrl, text="◀", width=28, height=28,
                          font=ctk.CTkFont(size=12),
                          fg_color=BTN, hover_color=BTN_HOV,
                          border_color=BORDER, border_width=1,
                          text_color=GOLD, corner_radius=4,
                          command=(lambda ii=i: self._move(ii, 1))).pack(side="left", padx=2)

            self._make_val_label(ctrl, i)

            ctk.CTkButton(ctrl, text="▶", width=28, height=28,
                          font=ctk.CTkFont(size=12),
                          fg_color=BTN, hover_color=BTN_HOV,
                          border_color=BORDER, border_width=1,
                          text_color=GOLD, corner_radius=4,
                          command=(lambda ii=i: self._move(ii, -1))).pack(side="left", padx=2)

        # Solve button
        solve_f = ctk.CTkFrame(self, fg_color="transparent")
        solve_f.pack(fill="x", padx=14, pady=6)
        self.solve_btn = ctk.CTkButton(solve_f, text=t["solve_btn"],
                                        font=ctk.CTkFont(size=13, weight="bold"),
                                        height=40, corner_radius=7,
                                        fg_color=GOLD, hover_color=GOLD2,
                                        text_color=BG, command=self._solve)
        self.solve_btn.pack(side="left", fill="x", expand=True, padx=(0,6))
        self.reset_btn = ctk.CTkButton(solve_f, text=t["reset_btn"], width=90, height=40,
                      font=ctk.CTkFont(size=12, weight="bold"), corner_radius=7,
                      fg_color=RED_MUTED, hover_color=RED_MUTED2,
                      border_color="#8a3030", border_width=1,
                      text_color="#e8a0a0", command=self._reset_pos)
        self.reset_btn.pack(side="left")

        # Status
        self.status_lbl = ctk.CTkLabel(self, text=t["status_init"],
                                        font=ctk.CTkFont(size=11), text_color=MUTED)
        self.status_lbl.pack(pady=(0,4))

        # Playback controls
        self.pb_frame = ctk.CTkFrame(self, fg_color="transparent")
        self.pb_frame.pack(fill="x", padx=14, pady=(0,4))
        self.pb_prev = ctk.CTkButton(self.pb_frame, text=t["pb_prev"], width=90, height=28,
                                      font=ctk.CTkFont(size=11),
                                      fg_color=BTN, hover_color=BTN_HOV,
                                      border_color=BORDER, border_width=1,
                                      text_color=TEXT, state="disabled",
                                      command=self._pb_prev)
        self.pb_prev.pack(side="left", padx=2)
        self.pb_lbl = ctk.CTkLabel(self.pb_frame, text=t["pb_step"].format(0, 0),
                                    font=ctk.CTkFont(size=11), text_color=MUTED, width=80)
        self.pb_lbl.pack(side="left", padx=6)
        self.pb_next = ctk.CTkButton(self.pb_frame, text=t["pb_next"], width=90, height=28,
                                      font=ctk.CTkFont(size=11),
                                      fg_color=BTN, hover_color=BTN_HOV,
                                      border_color=BORDER, border_width=1,
                                      text_color=TEXT, state="disabled",
                                      command=self._pb_next)
        self.pb_next.pack(side="left", padx=2)
        self.pb_rst = ctk.CTkButton(self.pb_frame, text="↺", width=36, height=28,
                                     font=ctk.CTkFont(size=13),
                                     fg_color=BTN, hover_color=BTN_HOV,
                                     border_color=BORDER, border_width=1,
                                     text_color=TEXT, state="disabled",
                                     command=self._pb_reset)
        self.pb_rst.pack(side="left", padx=2)

        # Support button (packed at the bottom first to ensure it's always visible)
        self.support_btn = ctk.CTkButton(
            self, text=t["support_btn"],
            font=ctk.CTkFont(size=11, weight="bold"),
            fg_color=BTN, hover_color=BTN_HOV,
            border_color=BORDER, border_width=1,
            text_color=GOLD, height=30, corner_radius=5,
            command=self._open_support
        )
        self.support_btn.pack(side="bottom", fill="x", padx=14, pady=(4,12))

        # Steps list
        steps_outer = ctk.CTkFrame(self, fg_color=PANEL,
                                    border_color=BORDER, border_width=1, corner_radius=8)
        steps_outer.pack(fill="both", expand=True, padx=14, pady=(0,4))
        self.steps_title_lbl = ctk.CTkLabel(steps_outer, text=t["steps_header"],
                     font=ctk.CTkFont(size=10, weight="bold"),
                     text_color=MUTED)
        self.steps_title_lbl.pack(anchor="w", padx=12, pady=(8,4))
        self.steps_scroll = ctk.CTkScrollableFrame(steps_outer, fg_color="transparent")
        self.steps_scroll.pack(fill="both", expand=True, padx=8, pady=(0,8))

    def _make_val_label(self, parent, i):
        lbl = ctk.CTkLabel(parent, text="0", font=ctk.CTkFont(size=12, weight="bold", family="Courier"),
                            text_color=RED_PIN, width=28)
        lbl.pack(side="left", padx=2)
        if not hasattr(self, '_val_labels'):
            self._val_labels = {}
        self._val_labels[i] = lbl
        self._update_val_label(i)

    def _update_val_label(self, i):
        if not hasattr(self, '_val_labels') or i not in self._val_labels: return
        v = self.plate_canvases[i].value
        lbl = self._val_labels[i]
        txt = f"+{v}" if v > 0 else str(v)
        col = RED_PIN if v == 0 else YELLOW_PIN
        lbl.configure(text=txt, text_color=col)

    def _move(self, i, delta):
        self.plate_canvases[i].adjust(delta)
        self._update_val_label(i)
        self._clear_solution()

    def _on_plate_change(self):
        self._clear_solution()

    def _clear_solution(self):
        self.solution = []
        self._start_state = None
        self.pb_states = []
        self.pb_idx = -1
        for w in self.steps_scroll.winfo_children(): w.destroy()
        self.step_frames = []
        self._update_pb_btns()
        t = TRANSLATIONS[self.lang]
        self.status_lbl.configure(text=t["status_changed"], text_color=MUTED)

    def _update_segmented_button_contrast(self, seg_btn):
        selected = seg_btn.get()
        if not hasattr(seg_btn, '_buttons_dict') or not seg_btn._buttons_dict:
            return
        for val, btn in seg_btn._buttons_dict.items():
            if val == selected:
                btn.configure(text_color=BG)
            else:
                btn.configure(text_color=TEXT)

    def _on_lang_change(self, new_lang):
        self.lang = new_lang
        self._update_ui_text()
        self._update_segmented_button_contrast(self.lang_btn)

    def _update_ui_text(self):
        t = TRANSLATIONS[self.lang]

        # Main Window Title and Header
        self.title(t["title"])
        self.hdr_title_lbl.configure(text=t["hdr_title"])
        self.rules_btn.configure(text=t["rules_btn"])

        # Always on top switcher update
        self.topmost_btn.configure(values=t["topmost_opts"])
        self.topmost_btn.set(t["topmost_opts"][1] if self._topmost else t["topmost_opts"][0])

        self._update_segmented_button_contrast(self.lang_btn)
        self._update_segmented_button_contrast(self.topmost_btn)

        self.leg_title_lbl.configure(text=t["legend_title"])
        for lbl, key in self.leg_labels:
            lbl.configure(text=t[key])

        for lbl, idx in self.row_labels:
            lbl.configure(text=t["plate_short"].format(idx + 1))

        # Solve button text (depends on state)
        if self.solve_btn.cget("state") == "disabled" and self.solve_btn.cget("text") in [TRANSLATIONS["RU"]["solve_searching"], TRANSLATIONS["EN"]["solve_searching"]]:
            self.solve_btn.configure(text=t["solve_searching"])
        else:
            self.solve_btn.configure(text=t["solve_btn"])

        self.reset_btn.configure(text=t["reset_btn"])

        # Status Label update (needs context mapping)
        curr_status = self.status_lbl.cget("text")
        if curr_status in [TRANSLATIONS["RU"]["status_init"], TRANSLATIONS["EN"]["status_init"]]:
            self.status_lbl.configure(text=t["status_init"])
        elif curr_status in [TRANSLATIONS["RU"]["status_reset"], TRANSLATIONS["EN"]["status_reset"]]:
            self.status_lbl.configure(text=t["status_reset"])
        elif curr_status in [TRANSLATIONS["RU"]["status_changed"], TRANSLATIONS["EN"]["status_changed"]]:
            self.status_lbl.configure(text=t["status_changed"])
        elif curr_status in [TRANSLATIONS["RU"]["status_no_solution"], TRANSLATIONS["EN"]["status_no_solution"]]:
            self.status_lbl.configure(text=t["status_no_solution"])
        elif curr_status in [TRANSLATIONS["RU"]["status_already_solved"], TRANSLATIONS["EN"]["status_already_solved"]]:
            self.status_lbl.configure(text=t["status_already_solved"])
        elif curr_status in [TRANSLATIONS["RU"]["status_rules_saved"], TRANSLATIONS["EN"]["status_rules_saved"]]:
            self.status_lbl.configure(text=t["status_rules_saved"])
        elif "Найдено:" in curr_status or "Found:" in curr_status:
            import re
            m = re.search(r'\d+', curr_status)
            if m:
                steps_cnt = m.group(0)
                self.status_lbl.configure(text=t["status_solved"].format(steps_cnt))

        # Playback
        self.pb_prev.configure(text=t["pb_prev"])
        self.pb_next.configure(text=t["pb_next"])
        pb_lbl_txt = self.pb_lbl.cget("text")
        if "/" in pb_lbl_txt:
            parts = pb_lbl_txt.replace("шаг ", "").replace("step ", "").split("/")
            if len(parts) == 2:
                self.pb_lbl.configure(text=t["pb_step"].format(parts[0], parts[1]))

        self.steps_title_lbl.configure(text=t["steps_header"])

        if self.solution:
            self._render_solution_steps()

        # Translate support button
        if hasattr(self, 'support_btn') and self.support_btn:
            self.support_btn.configure(text=t["support_btn"])

        # If rules window is active, destroy and reopen it at same position (automatically applies new language)
        if hasattr(self, '_rules_win') and self._rules_win.winfo_exists():
            try:
                self._rules_win_pos = (self._rules_win.winfo_x(), self._rules_win.winfo_y())
            except Exception:
                pass
            self._rules_win.destroy()
            self._open_rules()

        # If support window is active, destroy and reopen it at same position (automatically applies new language)
        if hasattr(self, '_support_win') and self._support_win.winfo_exists():
            try:
                self._support_win_pos = (self._support_win.winfo_x(), self._support_win.winfo_y())
            except Exception:
                pass
            self._support_win.destroy()
            self._open_support()

    def _render_solution_steps(self):
        for w in self.steps_scroll.winfo_children(): w.destroy()
        self.step_frames = []
        t = TRANSLATIONS[self.lang]
        if not hasattr(self, '_start_state') or self._start_state is None:
            return
        cur = self._start_state
        for i, (plate, direction) in enumerate(self.solution):
            nxt = apply_move(cur, plate, direction, self.rules)
            state_str = "  ".join(f"+{v}" if v > 0 else str(v) for v in nxt)
            row = ctk.CTkFrame(self.steps_scroll, fg_color="transparent", corner_radius=4)
            row.pack(fill="x", pady=1)
            ctk.CTkLabel(row, text=f"{i+1:>2}.", width=26,
                         font=ctk.CTkFont(size=11), text_color=MUTED).pack(side="left")
            ctk.CTkLabel(row, text=f"{t['step_plate']} {plate+1}", width=88,
                         font=ctk.CTkFont(size=12, weight="bold"), text_color=GOLD).pack(side="left")
            dir_col = BLUE_DIR if direction == 1 else RED_DIR
            dir_txt = t["step_left"] if direction == 1 else t["step_right"]
            ctk.CTkLabel(row, text=dir_txt, width=88,
                         font=ctk.CTkFont(size=12, weight="bold"), text_color=dir_col).pack(side="left", padx=4)
            ctk.CTkLabel(row, text=f"[{state_str}]",
                         font=ctk.CTkFont(size=11, family="Courier"), text_color=MUTED).pack(side="left", padx=6)
            self.step_frames.append(row)
            cur = nxt
        if self.pb_idx >= 0:
            self._highlight_step(self.pb_idx)

    def _solve(self):
        start = [pc.value for pc in self.plate_canvases]
        self._start_state = tuple(start)
        t = TRANSLATIONS[self.lang]
        self.solve_btn.configure(text=t["solve_searching"], state="disabled")
        self.update()
        path = bfs(start, self.n_plates, self.rules)
        self.solve_btn.configure(text=t["solve_btn"], state="normal")
        for w in self.steps_scroll.winfo_children(): w.destroy()
        self.step_frames = []
        if path is None:
            self.status_lbl.configure(text=t["status_no_solution"], text_color=RED_PIN)
            return
        if len(path) == 0:
            self.status_lbl.configure(text=t["status_already_solved"], text_color=RED_PIN)
            return
        self.solution = path
        self.pb_states = [tuple(start)]
        s = tuple(start)
        for plate, direction in path:
            s = apply_move(s, plate, direction, self.rules)
            self.pb_states.append(s)
        self.pb_idx = -1
        self.status_lbl.configure(text=t["status_solved"].format(len(path)), text_color="#4a9a4a")

        self._render_solution_steps()

        self.pb_lbl.configure(text=t["pb_step"].format(0, len(path)))
        self._update_pb_btns()

    def _pb_next(self):
        if self.pb_idx < len(self.solution) - 1:
            self.pb_idx += 1
            self._apply_pb_state(self.pb_idx + 1)
            self._highlight_step(self.pb_idx)
            t = TRANSLATIONS[self.lang]
            self.pb_lbl.configure(text=t["pb_step"].format(self.pb_idx+1, len(self.solution)))
        self._update_pb_btns()

    def _pb_prev(self):
        if self.pb_idx >= 0:
            self._apply_pb_state(self.pb_idx)
            self.pb_idx -= 1
            self._highlight_step(self.pb_idx)
            t = TRANSLATIONS[self.lang]
            self.pb_lbl.configure(text=t["pb_step"].format(self.pb_idx+1, len(self.solution)))
        self._update_pb_btns()

    def _pb_reset(self):
        self.pb_idx = -1
        self._apply_pb_state(0)
        t = TRANSLATIONS[self.lang]
        self.pb_lbl.configure(text=t["pb_step"].format(0, len(self.solution)))
        for f in self.step_frames: f.configure(fg_color="transparent")
        self._update_pb_btns()

    def _apply_pb_state(self, idx):
        s = self.pb_states[idx]
        for i, pc in enumerate(self.plate_canvases):
            pc.set_value(s[i])
            self._update_val_label(i)

    def _highlight_step(self, idx):
        for i, f in enumerate(self.step_frames):
            f.configure(fg_color=BTN_HOV if i == idx else "transparent")
        if 0 <= idx < len(self.step_frames):
            self.step_frames[idx].update_idletasks()

    def _update_pb_btns(self):
        has = len(self.solution) > 0
        self.pb_prev.configure(state="normal" if has and self.pb_idx >= 0 else "disabled")
        self.pb_next.configure(state="normal" if has and self.pb_idx < len(self.solution)-1 else "disabled")
        self.pb_rst.configure(state="normal" if has else "disabled")

    def _reset_pos(self):
        """Сбрасывает положение всех пластин и правила замка."""
        # Сброс позиций
        for pc in self.plate_canvases:
            pc.set_value(0)
            self._update_val_label(self.plate_canvases.index(pc))
        # Сброс правил — каждая пластина движет только саму себя
        self.rules = [[(i, 1)] for i in range(self.n_plates)]
        self._clear_solution()
        t = TRANSLATIONS[self.lang]
        self.status_lbl.configure(
            text=t["status_reset"],
            text_color=MUTED)

    def _on_topmost_change(self, value):
        t = TRANSLATIONS[self.lang]
        self._topmost = (value == t["topmost_opts"][1])
        self.attributes('-topmost', self._topmost)
        # Распространяем и на окно правил если оно открыто
        if hasattr(self, '_rules_win'):
            try:
                if self._rules_win.winfo_exists():
                    self._rules_win.attributes('-topmost', self._topmost)
            except Exception:
                pass
        self._update_segmented_button_contrast(self.topmost_btn)

    def _open_rules(self):
        # Не открывать второй экземпляр
        if hasattr(self, '_rules_win'):
            try:
                if self._rules_win.winfo_exists():
                    self._rules_win.lift()
                    self._rules_win.focus_force()
                    return
            except Exception:
                pass

        t = TRANSLATIONS[self.lang]
        win = ctk.CTkToplevel(self)
        self._rules_win = win
        win.title(t["rw_title"])
        win.configure(fg_color=BG)
        win.transient(self)
        win.lift()
        win.focus_force()
        win.attributes('-topmost', True)
        win.after(300, lambda: win.attributes('-topmost', self._topmost))
        win.after(200, lambda: _apply_dark_titlebar(win))

        # Позиционирование: если есть запомненные координаты — открыть там,
        # иначе — рядом с главным окном
        if hasattr(self, '_rules_win_pos'):
            rx, ry = self._rules_win_pos
            win.geometry(f"580x500+{rx}+{ry}")
        else:
            self.update_idletasks()
            mx = self.winfo_x()
            my = self.winfo_y()
            win.geometry(f"580x500+{mx + 40}+{my + 30}")

        def _save_pos_and_close():
            try:
                self._rules_win_pos = (win.winfo_x(), win.winfo_y())
            except Exception:
                pass
            win.destroy()

        win.protocol("WM_DELETE_WINDOW", _save_pos_and_close)

        ctk.CTkLabel(win, text=t["rw_header"],
                     font=ctk.CTkFont(size=14, weight="bold"),
                     text_color=GOLD).pack(pady=(14,4))
        ctk.CTkLabel(win, text=t["rw_subtitle"],
                     font=ctk.CTkFont(size=11), text_color=MUTED).pack(pady=(0,6))

        # Scrollable area через tk.Canvas
        scroll_outer = tk.Frame(win, bg=BORDER, bd=1, relief="flat")
        scroll_outer.pack(fill="both", expand=True, padx=14, pady=4)

        canvas = tk.Canvas(scroll_outer, bg=PANEL, highlightthickness=0)
        sb = tk.Scrollbar(scroll_outer, orient="vertical", command=canvas.yview)
        canvas.configure(yscrollcommand=sb.set)
        sb.pack(side="right", fill="y")
        canvas.pack(side="left", fill="both", expand=True)

        inner = tk.Frame(canvas, bg=PANEL)
        win_id = canvas.create_window((0, 0), window=inner, anchor="nw")

        def _on_inner_configure(e):
            canvas.configure(scrollregion=canvas.bbox("all"))
        def _on_canvas_configure(e):
            canvas.itemconfig(win_id, width=e.width)
        inner.bind("<Configure>", _on_inner_configure)
        canvas.bind("<Configure>", _on_canvas_configure)

        # MouseWheel только для этого окна, убирается при закрытии
        def _on_scroll(e):
            canvas.yview_scroll(int(-1 * (e.delta / 120)), "units")
        win.bind("<MouseWheel>", _on_scroll)

        effect_widgets = []
        for p in range(self.n_plates):
            grp = tk.Frame(inner, bg=PANEL)
            grp.pack(fill="x", padx=6, pady=3, anchor="nw")

            tk.Label(grp, text=t["rw_plate_left"].format(p+1),
                     font=("Courier", 11, "bold"),
                     fg=GOLD2, bg=PANEL, width=12, anchor="w").pack(side="left")

            ef_f = tk.Frame(grp, bg=PANEL)
            ef_f.pack(side="left", fill="x", expand=True)

            rows = []
            existing = [(pp, d) for pp, d in self.rules[p] if pp != p]
            for pp, d in existing:
                self._add_effect_row(ef_f, rows, self.n_plates, pp, d, exclude_p=p)
            effect_widgets.append((p, ef_f, rows))

            ctk.CTkButton(grp, text="+", width=26, height=26,
                          fg_color=BTN, hover_color=BTN_HOV,
                          text_color=GOLD, border_color=BORDER, border_width=1,
                          command=lambda ef=ef_f, rr=rows, cp=p: self._add_effect_row(
                              ef, rr, self.n_plates,
                              # default = первая доступная пластина (не текущая)
                              0 if cp != 0 else 1,
                              1, exclude_p=cp)
                          ).pack(side="left", padx=6)

            tk.Frame(inner, bg=BORDER, height=1).pack(fill="x", padx=6)

        def save_rules():
            new_rules = []
            for p, ef_f, rows in effect_widgets:
                effects = [(p, 1)]
                for cb_plate, cb_dir in rows:
                    try:
                        pp = int(cb_plate.get().strip()) - 1
                        # Поддерживаем и русскую, и английскую версию направления
                        d = 1 if cb_dir.get().strip() in ["влево", "left"] else -1
                        if 0 <= pp < self.n_plates and pp != p:
                            effects.append((pp, d))
                    except Exception:
                        pass
                new_rules.append(effects)
            self.rules = new_rules
            self.status_lbl.configure(
                text=t["status_rules_saved"],
                text_color=GOLD)
            _save_pos_and_close()

        ctk.CTkButton(win, text=t["rw_save"], height=36,
                      font=ctk.CTkFont(size=13, weight="bold"),
                      fg_color=GOLD, hover_color=GOLD2, text_color=BG, corner_radius=6,
                      command=save_rules).pack(pady=10, padx=14, fill="x")

    def _add_effect_row(self, parent, rows, n, default_p, default_d, exclude_p=None):
        row_f = tk.Frame(parent, bg=PANEL)
        row_f.pack(fill="x", pady=2)

        t = TRANSLATIONS[self.lang]

        tk.Label(row_f, text=t["rw_moves"], font=("Arial", 10),
                 fg=MUTED, bg=PANEL).pack(side="left", padx=(0,2))

        # Исключаем текущую пластину из списка — самоссылки невозможны
        available = [str(i+1) for i in range(n) if i != exclude_p]
        # Дефолтное значение: если default_p совпадает с exclude_p, берём первую доступную
        default_str = str(default_p + 1) if str(default_p + 1) in available else (available[0] if available else "1")

        cb_plate = ttk.Combobox(row_f, values=available,
            width=4, state="readonly", style='Dark.TCombobox')
        cb_plate.set(default_str)
        cb_plate.pack(side="left", padx=3)

        cb_dir = ttk.Combobox(row_f,
            values=[t["rw_left"], t["rw_right"]],
            width=8, state="readonly", style='Dark.TCombobox')
        cb_dir.set(t["rw_left"] if default_d == 1 else t["rw_right"])
        cb_dir.pack(side="left", padx=3)

        entry = (cb_plate, cb_dir)

        def remove(rf=row_f, e=entry):
            rf.destroy()
            if e in rows:
                rows.remove(e)

        tk.Button(row_f, text="✕", width=2,
                  bg=BTN, fg=MUTED, activebackground="#5a2020", activeforeground=TEXT,
                  relief="flat", font=("Arial", 10), bd=0,
                  command=remove).pack(side="left", padx=2)

        rows.append(entry)

    def _open_support(self):
        # Prevent opening multiple instances
        if hasattr(self, '_support_win'):
            try:
                if self._support_win.winfo_exists():
                    self._support_win.lift()
                    self._support_win.focus_force()
                    return
            except Exception:
                pass

        t = TRANSLATIONS[self.lang]
        win = ctk.CTkToplevel(self)
        self._support_win = win
        win.title(t["sup_title"])
        win.configure(fg_color=BG)
        win.transient(self)
        win.lift()
        win.focus_force()
        win.resizable(False, False)
        win.attributes('-topmost', True)
        win.after(300, lambda: win.attributes('-topmost', self._topmost))
        win.after(200, lambda: _apply_dark_titlebar(win))

        # Center relative to main window
        self.update_idletasks()
        mx = self.winfo_x()
        my = self.winfo_y()
        mw = self.winfo_width()
        mh = self.winfo_height()
        rx = mx + (mw - 460) // 2
        ry = my + (mh - 380) // 2
        win.geometry(f"460x380+{rx}+{ry}")

        ctk.CTkLabel(win, text=t["sup_header"],
                     font=ctk.CTkFont(size=14, weight="bold"),
                     text_color=GOLD).pack(pady=(18,6))

        # Description
        desc = ctk.CTkLabel(win, text=t["sup_desc"],
                            font=ctk.CTkFont(size=11), text_color=TEXT,
                            wraplength=420, justify="center")
        desc.pack(pady=(0,16), padx=20)

        # Donation rows
        rows = [
            ("BNB (BSC)", DONATE_BNB),
            ("Ethereum (ERC-20)", DONATE_ETH),
            ("Solana", DONATE_SOL),
            ("TON", DONATE_TON)
        ]

        for label_text, val in rows:
            row = ctk.CTkFrame(win, fg_color=PANEL, border_color=BORDER, border_width=1, corner_radius=6)
            row.pack(fill="x", padx=20, pady=4)

            # Left label
            lbl = ctk.CTkLabel(row, text=label_text, font=ctk.CTkFont(size=11, weight="bold"),
                               text_color=GOLD, width=130, anchor="w")
            lbl.pack(side="left", padx=(10,4), pady=8)

            # Middle entry (read-only)
            ent = ctk.CTkEntry(row, height=26, font=ctk.CTkFont(size=10, family="Courier"),
                               fg_color=HOLE_BG, border_color=BORDER, text_color=TEXT,
                               corner_radius=4)
            ent.insert(0, val)
            ent.configure(state="readonly")
            ent.pack(side="left", fill="x", expand=True, padx=4)

            # Right copy button
            btn = ctk.CTkButton(row, text=t["sup_copy"], width=80, height=26,
                                font=ctk.CTkFont(size=10, weight="bold"),
                                fg_color=BTN, hover_color=BTN_HOV,
                                border_color=BORDER, border_width=1,
                                text_color=GOLD, corner_radius=4)
            btn.pack(side="right", padx=10)

            # Setup command for copying
            def make_copy_cmd(v=val, b=btn):
                return lambda: self._copy_to_clipboard(v, b)
            btn.configure(command=make_copy_cmd(val, btn))

    def _copy_to_clipboard(self, text, button):
        self.clipboard_clear()
        self.clipboard_append(text)
        self.update()

        t = TRANSLATIONS[self.lang]
        button.configure(text=t["sup_copied"], text_color="#a0e0a0", fg_color="#1e3a1e", border_color="#306030")

        def restore(b=button):
            try:
                b.configure(text=t["sup_copy"], text_color=GOLD, fg_color=BTN, border_color=BORDER)
            except Exception:
                pass
        self.after(1500, restore)


if __name__ == "__main__":
    app = App()
    app.mainloop()
