import win32gui
import win32con
import win32clipboard as w

def send_message_to_window(window_title, message):
    # 验证窗口标题的合法性
    if not isinstance(window_title, str) or not window_title:
        raise ValueError("Window title must be a non-empty string.")

    # 验证消息的合法性
    if not isinstance(message, str) or not message:
        raise ValueError("Message must be a non-empty string.")

    # 将消息复制到剪贴板中
    w.OpenClipboard()
    w.EmptyClipboard()
    w.SetClipboardData(win32con.CF_UNICODETEXT, message)
    w.CloseClipboard()

    # 获取窗口句柄
    handle = win32gui.FindWindow(None, window_title)

    # 判断是否找到窗口
    if not handle:
        raise ValueError("Window '{}' not found.".format(window_title))

    # 向窗口发送消息
    win32gui.SendMessage(handle, 770, 0, 0)
    win32gui.SendMessage(handle, win32con.WM_KEYDOWN, win32con.VK_RETURN, 0)
