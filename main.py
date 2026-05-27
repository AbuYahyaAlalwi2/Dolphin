import logging
from agents.thinker import process_command
from agents.executor import execute_action

# إعداد السجلات (Logs) لمراقبة تصرفات دولفين
logging.basicConfig(filename='logs/system.log', level=logging.INFO)

def main_orchestrator(user_input):
    try:
        # 1. التفكير: دولفين يحلل الأمر
        task = process_command(user_input)
        
        # 2. التنفيذ: دولفين ينفذ الأمر عبر الأداة المناسبة
        result = execute_action(task)
        
        return f"✅ تم التنفيذ بنجاح: {result}"
    except Exception as e:
        logging.error(f"خطأ في التنفيذ: {e}")
        return f"❌ فشلت المهمة: {e}"

# هذا هو المحرك الذي سيربط تليجرام بالموزع
if __name__ == "__main__":
    print("نظام دولفين المركزي يعمل...")