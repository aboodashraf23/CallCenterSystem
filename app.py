from flask import Flask, request

app = Flask(__name__)

# =========================
# 📦 بيانات Just Bakery + تواريخ إنتاج
# =========================
products = [
    {"name": "menin", "qty": 5.5, "date": "2026-06-18"},
    {"name": "cookies vanilla", "qty": 3.5, "date": "2026-06-17"},
    {"name": "cookies chocolate", "qty": 6, "date": "2026-06-19"},
    {"name": "brown chips", "qty": 7, "date": "2026-06-20"},
    {"name": "brown menin", "qty": 4.6, "date": "2026-06-20"},
    {"name": "brown breadstickes", "qty": 6, "date": "2026-06-16"},
    {"name": "rusk", "qty": 8, "date": "2026-06-15"},
    {"name": "rusk slim with sesame", "qty": 0, "date": "2026-06-18"},
    {"name": "rusk with sesame", "qty": 4.5, "date": "2026-06-17"},
    {"name": "menin with filled agwa", "qty": 9, "date": "2026-06-19"},
    {"name": "oras with filled agwa", "qty": 7, "date": "2026-06-20"},
    {"name": "brown rusk", "qty": 2.5, "date": "2026-06-20"},
    {"name": "palmeh", "qty": 6, "date": "2026-06-16"},
    {"name": "toast brown", "qty": 8, "date": "2026-06-15"},
    {"name": "donut mini ring nutella", "qty": 20, "date": "2026-06-18"},
    {"name": "donut mini ring lotus", "qty": 10, "date": "2026-06-17"},
    {"name": "donut mini ring pistachio", "qty": 5, "date": "2026-06-19"},
    {"name": "donut mini filled with nutella", "qty": 18, "date": "2026-06-20"},
    {"name": "donut mini filled with lotus", "qty": 8, "date": "2026-06-20"},
    {"name": "donut mini filled with pistachio", "qty": 4, "date": "2026-06-16"},
    {"name": "donut large ring nutella", "qty": 14, "date": "2026-06-15"},
    {"name": "donut large ring lotus", "qty": 4, "date": "2026-06-18"},
    {"name": "donut large ring pistachio", "qty": 2, "date": "2026-06-17"},
    {"name": "donut large filled with nutella", "qty": 9, "date": "2026-06-19"},
    {"name": "donut large filled with lotus", "qty": 3, "date": "2026-06-20"},
    {"name": "donut large filled with pistachio", "qty": 1, "date": "2026-06-20"},
    {"name": "palmeh", "qty": 6, "date": "2026-06-16"},
    {"name": "toast brown", "qty": 8, "date": "2026-06-15"},
    {"name": "croissant plain", "qty": 30, "date": "2026-06-18"},
    {"name": "croissant istanbuly cheese", "qty": 10, "date": "2026-06-17"},
    {"name": "croissant roumy cheese", "qty": 16, "date": "2026-06-19"},
    {"name": "pate feta", "qty": 9, "date": "2026-06-20"},
    {"name": "pate roumy cheese", "qty": 8, "date": "2026-06-20"},
    {"name": "pate sausage", "qty": 12, "date": "2026-06-16"},
    {"name": "pate pepperoni", "qty": 14, "date": "2026-06-15"},
    {"name": "pate turkey chedder", "qty": 20, "date": "2026-06-18"},
    {"name": "pain suasse", "qty": 6, "date": "2026-06-17"},
    {"name": "pizza piece", "qty": 15, "date": "2026-06-19"},
    {"name": "mini pizza", "qty": 3, "date": "2026-06-20"},
    {"name": "oras", "qty": 2.5, "date": "2026-06-20"},
    {"name": "borek with filled istanbuly cheese", "qty": 6, "date": "2026-06-16"},
    {"name": "pizza triangle", "qty": 2, "date": "2026-06-15"},
    {"name": "mini pate istanbuly", "qty": 3.7, "date": "2026-06-15"},
    {"name": "mini pate sausage", "qty": 20, "date": "2026-06-18"},
    {"name": "mini pate roumy", "qty": 6, "date": "2026-06-17"},
    {"name": "danish fruits", "qty": 5, "date": "2026-06-19"},
    {"name": "danish rasian mango", "qty": 4, "date": "2026-06-20"},
    {"name": "tart bluberry", "qty": 4, "date": "2026-06-20"},
    {"name": "tart roseberry", "qty": 3, "date": "2026-06-16"},
    {"name": "croissant nutella", "qty": 4, "date": "2026-06-15"},
    {"name": "mini echlair nutella", "qty": 2, "date": "2026-06-15"},
    {"name": "mini echlair lotus", "qty": 1.2, "date": "2026-06-15"},
    {"name": "mini echlair dark choclate", "qty": 2.5, "date": "2026-06-18"},
    {"name": "petit pain - plain", "qty": 180, "date": "2026-06-17"},
    {"name": "large vienna - plain", "qty": 20, "date": "2026-06-19"},
    {"name": "burger bun with sesame 3 inch", "qty": 24, "date": "2026-06-20"},
    {"name": "burger bun with sesame 5 inch", "qty": 10, "date": "2026-06-20"},
    {"name": "petit pain - brown", "qty": 100, "date": "2026-06-16"},
    {"name": "medium vienna with oat - brown", "qty": 40, "date": "2026-06-15"},
]

# =========================
# 🌐 الصفحة الرئيسية
# =========================

@app.route("/")
def home():
    q = request.args.get("q", "")

    result = ""

    if q:
        found = False

        for p in products:
            if q.lower() in p["name"].lower():
                found = True

                qty = p["qty"]
                date = p["date"]

                # حالة المخزون
                if qty > 10:
                    status = "🟢 Available"
                elif qty > 0:
                    status = "🟡 Low Stock"
                else:
                    status = "🔴 Out of Stock"

                result += f"""
                <div style="
                    background:white;
                    padding:15px;
                    margin:10px auto;
                    width:350px;
                    border-radius:10px;
                    box-shadow:0 2px 6px rgba(0,0,0,0.1);
                    text-align:left;
                ">

                    <h3>🥐 {p['name']}</h3>

                    <p>📦 Quantity: <b>{qty}</b></p>

                    <p>📅 Production Date: <b>{date}</b></p>

                    <p>{status}</p>

                    <p style="color:#1e3a8a">Just Bakery System</p>
                </div>
                """

        if not found:
            result = "<p style='color:red'>❌ No product found</p>"

    return f"""
    <html>
    <body style="font-family:Arial;background:#f4f6f9;text-align:center">

        <h2 style="background:#1e3a8a;color:white;padding:15px">
            Just Bakery - Call Center System
        </h2>

        <form>
            <input name="q" placeholder="Search product..."
                style="padding:10px;width:300px;border-radius:5px;border:1px solid #ccc">
            <button style="padding:10px">Search</button>
        </form>

        <br>

        {result}

    </body>
    </html>
    """

# =========================
# ▶️ Run Server
# =========================
if __name__ == "__main__":
    app.run(debug=True)