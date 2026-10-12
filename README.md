# EDF Scheduling Algorithm

پیاده‌سازی الگوریتم زمان‌بندی **EDF (Earliest Deadline First)** برای درس سیستم‌های عامل.

## 📌 معرفی الگوریتم

الگوریتم EDF یک الگوریتم زمان‌بندی **Preemptive** و **Dynamic Priority** است که در سیستم‌های بی‌درنگ (Real-Time Systems) کاربرد دارد.

در این الگوریتم، هر لحظه تسکی که **نزدیک‌ترین Deadline** را دارد، برای اجرا انتخاب می‌شود. اگر تسک جدیدی با Deadline نزدیک‌تر وارد شود، تسک فعلی قطع شده و تسک جدید اجرا می‌شود.

## ⚙️ ویژگی‌ها

- **Preemptive**: تسک‌ها می‌توانند وسط اجرا قطع شوند
- **Dynamic Priority**: اولویت تسک‌ها بر اساس Deadline تغییر می‌کند
- **Optimal**: برای سیستم‌های تک‌پردازنده‌ای بهینه است
- **مناسب برای**: سیستم‌های Real-Time

## 🧮 فرمول‌های محاسبه

- **Waiting Time (WT)** = Finish Time - Arrival Time - Burst Time
- **Turnaround Time (TAT)** = Finish Time - Arrival Time
- **Utilization (U)** = مجموع Burst Timeها ÷ بزرگ‌ترین Deadline

## 📋 تسک‌های نمونه

| Task | Arrival | Burst | Deadline |
|------|---------|-------|----------|
| T1   | 0       | 3     | 7        |
| T2   | 1       | 2     | 5        |
| T3   | 2       | 1     | 4        |

## 🚀 نحوه اجرا

```bash
python edf.py
