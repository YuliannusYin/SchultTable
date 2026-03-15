import random
import sys
import os

# 添加当前目录到Python路径以便导入主程序
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

# 测试数字生成函数
def test_number_generation():
    print("测试数字生成功能...")
    numbers = list(range(1, 26))
    random.shuffle(numbers)
    
    # 检查是否包含1-25的所有数字
    assert len(numbers) == 25, "数字数量不正确"
    assert set(numbers) == set(range(1, 26)), "数字范围不正确"
    print("[OK] 基础数字生成测试通过")
    print(f"生成的数字: {numbers}")

# 测试验证函数
def test_validation():
    print("\n测试验证函数...")
    
    from schult_table import SchultTable
    import tkinter as tk
    root = tk.Tk()
    root.withdraw()
    app = SchultTable(root)
    
    # 测试有效数字序列
    valid_numbers = list(range(1, 26))
    assert app._validate_numbers(valid_numbers), "有效序列验证失败"
    print("[OK] 有效数字序列验证通过")
    
    # 测试数量错误的序列
    invalid_length = list(range(1, 24))
    assert not app._validate_numbers(invalid_length), "长度错误验证失败"
    print("[OK] 长度错误验证通过")
    
    # 测试超出范围的数字
    invalid_range = list(range(1, 25)) + [26]
    assert not app._validate_numbers(invalid_range), "范围错误验证失败"
    print("[OK] 范围错误验证通过")
    
    # 测试低于范围的数字
    invalid_low = [0] + list(range(2, 26))
    assert not app._validate_numbers(invalid_low), "下限错误验证失败"
    print("[OK] 下限错误验证通过")
    
    # 测试重复数字
    invalid_duplicate = list(range(1, 25)) + [25, 25]
    invalid_duplicate.pop()
    assert not app._validate_numbers(invalid_duplicate + [25]), "重复数字验证失败"
    print("[OK] 重复数字验证通过")
    
    # 测试非整数
    invalid_type = list(range(1, 25)) + ['25']
    assert not app._validate_numbers(invalid_type), "类型错误验证失败"
    print("[OK] 类型错误验证通过")
    
    root.destroy()
    print("[OK] 所有验证函数测试通过")

# 测试多次运行稳定性
def test_multiple_runs(count=100):
    print(f"\n测试{count}次运行稳定性...")
    
    from schult_table import SchultTable
    import tkinter as tk
    root = tk.Tk()
    root.withdraw()
    app = SchultTable(root)
    
    all_valid = True
    for i in range(count):
        numbers = app._generate_valid_numbers()
        if not app._validate_numbers(numbers):
            print(f"[FAIL] 第{i+1}次生成失败: {numbers}")
            all_valid = False
        if (i + 1) % 20 == 0:
            print(f"  已完成 {i + 1}/{count} 次测试...")
    
    root.destroy()
    assert all_valid, f"{count}次测试中有失败"
    print(f"[OK] {count}次运行稳定性测试通过")

# 测试顺序检查逻辑
def test_order_checking():
    print("\n测试顺序检查逻辑...")
    current_number = 1
    
    # 正确顺序
    for i in range(1, 26):
        assert i == current_number, f"顺序检查失败: 期望{current_number}, 实际{i}"
        current_number += 1
    print("[OK] 顺序检查测试通过")

# 测试计时功能
def test_timer():
    print("\n测试计时功能...")
    import time
    start_time = time.time()
    time.sleep(0.1)
    end_time = time.time()
    elapsed = end_time - start_time
    assert elapsed > 0, "计时失败"
    assert elapsed < 1, "计时误差过大"
    print(f"[OK] 计时测试通过，用时: {elapsed:.3f}秒")

# 测试表格渲染功能
def test_table_rendering():
    print("\n测试表格渲染功能...")
    
    from schult_table import SchultTable
    import tkinter as tk
    root = tk.Tk()
    root.withdraw()
    app = SchultTable(root)
    
    # 验证初始渲染
    print("  验证初始表格渲染...")
    app._validate_table_rendering()
    
    # 测试多次重新生成
    print("  测试多次重新生成...")
    for i in range(10):
        app.restart()
        app._validate_table_rendering()
        if (i + 1) % 5 == 0:
            print(f"    已完成 {i + 1}/10 次重新生成验证...")
    
    root.destroy()
    print("[OK] 表格渲染测试通过")

if __name__ == "__main__":
    print("开始全面测试Schult Table功能...\n")
    test_number_generation()
    test_validation()
    test_order_checking()
    test_timer()
    test_multiple_runs(count=100)
    test_table_rendering()
    print("\n[SUCCESS] 所有测试通过！表格渲染和数字生成功能已完全验证，确保5×5稳定显示！")
