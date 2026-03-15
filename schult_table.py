import tkinter as tk
import random
import time

class SchultTable:
    def __init__(self, root):
        self.root = root
        self.root.title("Schult Table - 视觉注意力训练")
        self.root.geometry("550x700")
        self.root.resizable(False, False)
        
        # 颜色配置
        self.bg_color = "#f0f0f0"
        self.button_color = "#ffffff"
        self.text_color = "#333333"
        self.easy_highlight_color = "#4CAF50"  # 绿色
        self.normal_highlight_color = "#9e9e9e"  # 浅灰色
        self.error_color = "#f44336"
        
        self.root.configure(bg=self.bg_color)
        
        # 初始化变量
        self.current_number = 1
        self.start_time = None
        self.end_time = None
        self.buttons = []
        self.numbers = []
        self.grid_size = 5  # 默认5×5
        self.difficulty = "normal"  # 默认普通难度
        
        # 创建界面元素
        self.create_widgets()
        self.generate_table()
    
    def create_widgets(self):
        """创建所有UI组件"""
        self._create_title()
        self._create_grid_size_selector()
        self._create_difficulty_selector()
        self._create_progress_display()
        self._create_table_frame()
        self._create_restart_button()
    
    def _create_title(self):
        """创建标题组件"""
        self.title_label = tk.Label(
            self.root, 
            text="Schult Table", 
            font=("Arial", 24, "bold"),
            bg=self.bg_color,
            fg=self.text_color
        )
        self.title_label.pack(pady=20)
    
    def _create_grid_size_selector(self):
        """创建网格大小选择器"""
        self.grid_size_frame = tk.Frame(self.root, bg=self.bg_color)
        self.grid_size_frame.pack(pady=10)
        
        self.grid_size_label = tk.Label(
            self.grid_size_frame, 
            text="网格大小:", 
            font=("Arial", 12),
            bg=self.bg_color,
            fg=self.text_color
        )
        self.grid_size_label.pack(side=tk.LEFT, padx=5)
        
        self.grid_size_var = tk.StringVar(value="5")
        self.grid_size_options = ["3", "4", "5", "6", "7"]
        
        for size in self.grid_size_options:
            radio = tk.Radiobutton(
                self.grid_size_frame, 
                text=f"{size}×{size}",
                variable=self.grid_size_var,
                value=size,
                font=("Arial", 10),
                bg=self.bg_color,
                fg=self.text_color,
                command=self.on_grid_size_change
            )
            radio.pack(side=tk.LEFT, padx=5)
    
    def _create_difficulty_selector(self):
        """创建难度选择器"""
        self.difficulty_frame = tk.Frame(self.root, bg=self.bg_color)
        self.difficulty_frame.pack(pady=10)
        
        self.difficulty_label = tk.Label(
            self.difficulty_frame, 
            text="难度:", 
            font=("Arial", 12),
            bg=self.bg_color,
            fg=self.text_color
        )
        self.difficulty_label.pack(side=tk.LEFT, padx=5)
        
        self.difficulty_var = tk.StringVar(value="normal")
        self.difficulty_options = [
            {"value": "easy", "label": "简单"},
            {"value": "normal", "label": "普通"},
            {"value": "hard", "label": "困难"}
        ]
        
        for option in self.difficulty_options:
            radio = tk.Radiobutton(
                self.difficulty_frame, 
                text=option["label"],
                variable=self.difficulty_var,
                value=option["value"],
                font=("Arial", 10),
                bg=self.bg_color,
                fg=self.text_color,
                command=self.on_difficulty_change
            )
            radio.pack(side=tk.LEFT, padx=10)
    
    def _create_progress_display(self):
        """创建进度和计时器显示"""
        # 进度标签
        max_num = self.grid_size ** 2
        self.progress_label = tk.Label(
            self.root, 
            text=f"请按顺序点击数字: 1 → 2 → 3 → ... → {max_num}", 
            font=("Arial", 12),
            bg=self.bg_color,
            fg=self.text_color
        )
        self.progress_label.pack(pady=10)
        
        # 计时器标签
        self.timer_label = tk.Label(
            self.root, 
            text="时间: 0.000秒", 
            font=("Arial", 14),
            bg=self.bg_color,
            fg=self.text_color
        )
        self.timer_label.pack(pady=10)
    
    def _create_table_frame(self):
        """创建表格框架"""
        self.table_frame = tk.Frame(self.root, bg=self.bg_color)
        self.table_frame.pack(pady=20)
    
    def _create_restart_button(self):
        """创建重新开始按钮"""
        self.restart_button = tk.Button(
            self.root, 
            text="重新开始", 
            font=("Arial", 12, "bold"),
            command=self.restart,
            bg="#2196F3",
            fg="white",
            padx=20,
            pady=10
        )
        self.restart_button.pack(pady=20)
    
    def generate_table(self):
        """生成并渲染表格"""
        # 清空表格
        for widget in self.table_frame.winfo_children():
            widget.destroy()
        
        # 生成随机数字
        self.numbers = self._generate_valid_numbers()
        
        # 创建网格
        self.buttons = []
        for i in range(self.grid_size):
            row = []
            for j in range(self.grid_size):
                num = self.numbers[i * self.grid_size + j]
                # 根据网格大小调整字体大小，增大字体以确保清晰可辨
                font_size = max(10, 16 - self.grid_size)
                button = tk.Button(
                    self.table_frame, 
                    text=str(num),
                    font=(("Arial", font_size, "bold")),
                    width=5,
                    height=2,
                    bg=self.button_color,
                    fg=self.text_color,
                    command=lambda n=num: self.on_button_click(n),
                    relief="solid",
                    bd=1
                )
                button.grid(row=i, column=j, padx=0, pady=0)
                row.append(button)
            self.buttons.append(row)
        
        # 验证表格是否正确渲染
        self._validate_table_rendering()
    
    def _generate_valid_numbers(self):
        """生成有效的随机数字序列"""
        max_num = self.grid_size ** 2
        numbers = list(range(1, max_num + 1))
        random.shuffle(numbers)
        return numbers
    
    def _validate_numbers(self, numbers):
        """验证数字序列是否有效"""
        max_num = self.grid_size ** 2
        # 检查数字数量
        if len(numbers) != max_num:
            return False
        
        # 检查是否包含1到max_num的所有数字且无重复
        expected = set(range(1, max_num + 1))
        actual = set(numbers)
        if actual != expected:
            return False
        
        # 检查每个数字的类型
        for num in numbers:
            if not isinstance(num, int):
                return False
        
        return True
    
    def _validate_table_rendering(self):
        # 验证按钮列表结构
        assert len(self.buttons) == self.grid_size, f"表格行数错误：期望{self.grid_size}行，实际{len(self.buttons)}行"
        
        for i, row in enumerate(self.buttons):
            assert len(row) == self.grid_size, f"第{i+1}行列数错误：期望{self.grid_size}列，实际{len(row)}列"
        
        # 验证实际渲染的组件数量
        expected_widgets = self.grid_size ** 2
        rendered_widgets = self.table_frame.winfo_children()
        assert len(rendered_widgets) == expected_widgets, f"渲染组件数量错误：期望{expected_widgets}个，实际{len(rendered_widgets)}个"
        
        # 验证所有按钮都有正确的数字
        displayed_numbers = []
        for row in self.buttons:
            for btn in row:
                num = int(btn['text'])
                displayed_numbers.append(num)
        
        expected_numbers = set(range(1, expected_widgets + 1))
        assert set(displayed_numbers) == expected_numbers, "显示的数字不完整或有重复"
        
        print(f"[OK] 表格渲染验证通过：{self.grid_size}×{self.grid_size}网格已正确显示")
    
    def on_button_click(self, number):
        """处理按钮点击事件"""
        self._start_timer_if_needed()
        
        if number == self.current_number:
            self._handle_correct_click(number)
        else:
            self._handle_incorrect_click(number)
    
    def _start_timer_if_needed(self):
        """如果是第一次点击，开始计时"""
        if self.current_number == 1 and self.start_time is None:
            self.start_time = time.time()
            self.update_timer()
    
    def _handle_correct_click(self, number):
        """处理正确的点击"""
        max_num = self.grid_size ** 2
        self._mark_button_as_clicked(number)
        self._update_progress(max_num)
        
        if self.current_number > max_num:
            self._handle_completion()
    
    def _mark_button_as_clicked(self, number):
        """标记已点击的按钮"""
        for i in range(self.grid_size):
            for j in range(self.grid_size):
                if int(self.buttons[i][j]['text']) == number:
                    self._configure_button_for_difficulty(self.buttons[i][j])
                    break
    
    def _configure_button_for_difficulty(self, button):
        """根据难度配置按钮样式"""
        if self.difficulty == "easy":
            # 简单难度：变为绿色
            button.configure(
                bg=self.easy_highlight_color, 
                fg="white",
                state=tk.DISABLED  # 禁用按钮
            )
        elif self.difficulty == "normal":
            # 普通难度：变为浅灰色
            button.configure(
                bg=self.normal_highlight_color, 
                fg="white",
                state=tk.DISABLED  # 禁用按钮
            )
        else:  # hard
            # 困难难度：无视觉反馈，仅禁用
            button.configure(
                state=tk.DISABLED  # 禁用按钮
            )
    
    def _update_progress(self, max_num):
        """更新进度"""
        self.current_number += 1
        if self.current_number <= max_num:
            self.progress_label.config(
                text=f"请按顺序点击数字: {self.current_number} → {self.current_number + 1} → ... → {max_num}"
            )
    
    def _handle_completion(self):
        """处理完成情况"""
        self.end_time = time.time()
        elapsed_time = self.end_time - self.start_time
        self.timer_label.config(
            text=f"完成! 用时: {elapsed_time:.3f}秒"
        )
        self.progress_label.config(
            text="训练完成! 点击重新开始按钮继续"
        )
    
    def _handle_incorrect_click(self, number):
        """处理错误的点击"""
        if self.difficulty == "easy":
            # 简单难度：短暂显示红色
            for i in range(self.grid_size):
                for j in range(self.grid_size):
                    if int(self.buttons[i][j]['text']) == number:
                        original_bg = self.buttons[i][j]['bg']
                        original_fg = self.buttons[i][j]['fg']
                        self.buttons[i][j].configure(
                            bg=self.error_color, 
                            fg="white"
                        )
                        # 0.7秒后恢复颜色
                        self.root.after(700, lambda btn=self.buttons[i][j], bg=original_bg, fg=original_fg: 
                            btn.configure(bg=bg, fg=fg)
                        )
                        break
        # 普通和困难难度：无反馈
    
    def update_timer(self):
        """更新计时器显示"""
        if self.start_time is not None and self.end_time is None:
            elapsed_time = time.time() - self.start_time
            self.timer_label.config(
                text=f"时间: {elapsed_time:.3f}秒"
            )
            self.root.after(10, self.update_timer)
    
    def on_grid_size_change(self):
        """处理网格大小变更"""
        try:
            # 更新网格大小
            size = int(self.grid_size_var.get())
            if size < 3 or size > 7:
                raise ValueError("网格大小必须在3到7之间")
            self.grid_size = size
            # 重置游戏状态
            self.restart()
        except ValueError as e:
            print(f"网格大小设置错误: {e}")
    
    def on_difficulty_change(self):
        """处理难度变更"""
        try:
            # 更新难度
            difficulty = self.difficulty_var.get()
            valid_difficulties = ["easy", "normal", "hard"]
            if difficulty not in valid_difficulties:
                raise ValueError(f"无效的难度值: {difficulty}")
            self.difficulty = difficulty
            # 重置游戏状态
            self.restart()
        except ValueError as e:
            print(f"难度设置错误: {e}")
    
    def restart(self):
        """重置游戏状态"""
        # 重置所有变量
        self.current_number = 1
        self.start_time = None
        self.end_time = None
        
        # 重置标签
        max_num = self.grid_size ** 2
        self.progress_label.config(
            text=f"请按顺序点击数字: 1 → 2 → 3 → ... → {max_num}"
        )
        self.timer_label.config(
            text="时间: 0.000秒"
        )
        
        # 重新生成表格
        self.generate_table()

if __name__ == "__main__":
    root = tk.Tk()
    app = SchultTable(root)
    root.mainloop()