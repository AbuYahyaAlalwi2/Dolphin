# بدلاً من مجرد حلقة while True الصامتة
print("دولفين في وضع الاستعداد وينتظر الأوامر...") # هذه الرسالة ستظهر في سجلات Render
while True:
    try:
        url = f"https://api.telegram.org/bot{TOKEN}/getUpdates?offset={last_update_id + 1}"
        response = requests.get(url).json()
        
        # إضافة طباعة بسيطة عند تلقي أي نبض من تليجرام
        if response.get('result'):
            print("تم استلام أمر جديد...") 
            # ... باقي الكود
    except Exception as e:
        print(f"حدث خطأ في الاتصال: {e}") # هذا سيكتب الخطأ في سجلات Render
    time.sleep(2)
