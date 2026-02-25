import json

# ---------- WELCOME ----------
print("🌾 WELCOME TO PARTH'S APP 💚 सबका स्मार्ट साथी 💚 🌾\n")

# ---------- FILE & DATA ----------
FILE = "parths_app_data.json"
try:
    with open(FILE, "r", encoding="utf-8") as f:
        data = json.load(f)
except:
    data = {}

def save():
    with open(FILE, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2, ensure_ascii=False)

# ---------- LANGUAGE ----------
def select_language():
    print("🌐 भाषा / Language: 1. हिंदी  2. English")
    choice = input("Choose: ").strip()
    return "hi" if choice=="1" else "en"

lang = select_language()

def show_msg(hi_msg, en_msg):
    print("\n"+(hi_msg if lang=="hi" else en_msg)+"\n")

# ---------- USER LOGIN ----------
def user_login():
    while True:
        username = input("Enter your name / नाम दर्ज करें: ").strip()
        if username:
            if "users" not in data:
                data["users"] = {}
            if username not in data["users"]:
                data["users"][username] = {"tools_used":[]}
            save()
            return username

current_user = user_login()
user_data = data["users"][current_user]

# ---------- CATEGORY SKELETON ----------
categories = {
    "1": {"name":"🌾 Crop Management", "tools":[]},
    "2": {"name":"💧 Irrigation Management", "tools":[]},
    "3": {"name":"🦠 Pest & Disease Control", "tools":[]},
    "4": {"name":"🌱 Organic & AI Farming", "tools":[]},
    "5": {"name":"🧴 Fertilizer Planning", "tools":[]},
    "6": {"name":"🌾 Seed Management", "tools":[]},
    "7": {"name":"📊 Profit & Yield Tracking", "tools":[]},
    "8": {"name":"💻 Smart Farming Tools", "tools":[]},
    "9": {"name":"📅 Crop Calendar", "tools":[]},
    "10":{"name":"🛠️ Farm Maintenance Tools", "tools":[]},
    "11":{"name":"📌 Reminders & Notes", "tools":[]}
}

# ---------- TOOLS PLACEHOLDERS ----------
import random
import json

# ---------- JSON functions for notes ----------
def save_notes(data, filename="notes.json"):
    with open(filename,"w") as f:
        json.dump(data,f)

def load_notes(filename="notes.json"):
    try:
        with open(filename,"r") as f:
            data = json.load(f)
        return data
    except:
        return {}

# ---------- CATEGORY 1: Crop Management Tools with Theory ----------

# 1️⃣ Crop Planner
def crop_planner():
    print("\n🌾 Crop Planner / फसल योजना 🌾")
    print("Theory / सिद्धांत: Helps farmers plan which crop to grow, how much water and fertilizer is needed. / किसान को यह तय करने में मदद करता है कि कौन सी फसल उगाई जाए और कितना पानी एवं उर्वरक चाहिए।")
    crop = input("Enter crop name / फसल का नाम: ")
    area = float(input("Enter field area in acres / क्षेत्रफल दर्ज करें: "))
    water_need = round(area * random.uniform(1200, 1800),1)
    fertilizer = random.choice(["NPK 20:20:20", "Urea 46%", "Compost"])
    print(f"💧 Recommended water for {crop}: {water_need} liters / {crop} के लिए पानी: {water_need} लीटर")
    print(f"🧴 Suggested fertilizer for {crop}: {fertilizer} / {crop} के लिए सुझावित उर्वरक: {fertilizer}")

# 2️⃣ Soil Health Check
def soil_health_check():
    print("\n🌱 Soil Health Check / मिट्टी स्वास्थ्य जांच 🌱")
    print("Theory / सिद्धांत: Checks moisture, pH and nutrients to know soil fertility. / मिट्टी की उर्वरता जानने के लिए नमी, पीएच और पोषक तत्व जांच।")
    moisture = random.randint(15, 80)
    ph = round(random.uniform(5.5,7.5),1)
    nutrients = random.choice(["Low 🔴","Medium 🟡","High 🟢"])
    print(f"💧 Soil Moisture: {moisture}% / मिट्टी नमी: {moisture}%")
    print(f"⚗️ PH Level: {ph} / पीएच स्तर: {ph}")
    print(f"🧴 Nutrient Level: {nutrients} / पोषक तत्व स्तर: {nutrients}")

# 3️⃣ Fertilizer Calculator
def fertilizer_calculator():
    print("\n🧴 Fertilizer Calculator / उर्वरक कैलकुलेटर 🧴")
    print("Theory / सिद्धांत: Suggests right fertilizer based on crop and soil type. / फसल और मिट्टी प्रकार के आधार पर सही उर्वरक सुझाता है।")
    crop = input("Enter crop name / फसल का नाम: ")
    soil_type = input("Enter soil type (Loamy/Clay/Sandy) / मिट्टी प्रकार: ")
    recommended = "NPK 20:20:20" if soil_type.lower()=="loamy" else "Urea 46%"
    print(f"Recommended fertilizer for {crop}: {recommended} / {crop} के लिए सुझाव: {recommended}")

# 4️⃣ Seed Calculator
def seed_calculator():
    print("\n🌱 Seed Calculator / बीज कैलकुलेटर 🌱")
    print("Theory / सिद्धांत: Estimates how much seed is needed for given area. / दिए गए क्षेत्रफल के लिए आवश्यक बीज की मात्रा का अनुमान।")
    crop = input("Enter crop name / फसल का नाम: ")
    area = float(input("Enter area in acres / क्षेत्रफल: "))
    seeds_needed = round(area * random.uniform(5,10),1)
    print(f"Estimated seeds required for {crop}: {seeds_needed} kg / {crop} के लिए अनुमानित बीज: {seeds_needed} किग्रा")

# 5️⃣ Irrigation Scheduler
def irrigation_scheduler():
    print("\n💧 Irrigation Scheduler / सिंचाई समय सारणी 💧")
    print("Theory / सिद्धांत: Plans when and how often to irrigate crops. / यह योजना बनाता है कि फसल को कब और कितनी बार सिंचाई करनी है।")
    crop = input("Enter crop name / फसल का नाम: ")
    area = float(input("Enter area in acres / क्षेत्रफल: "))
    frequency = random.choice(["Every 2 days / हर 2 दिन", "Every 3 days / हर 3 दिन", "Weekly / साप्ताहिक"])
    print(f"Recommended irrigation frequency for {crop}: {frequency}")

# 6️⃣ Crop Rotation
def crop_rotation():
    print("\n🔄 Crop Rotation Advisor / फसल रोटेशन सलाहकार 🔄")
    print("Theory / सिद्धांत: Rotating crops improves soil fertility and reduces pests. / फसल चक्रीकरण मिट्टी की उर्वरता बढ़ाता है और कीटों को कम करता है।")
    last_crop = input("Enter last crop grown / पिछली फसल: ")
    recommended = random.choice(["Legumes / दलहनी","Cereal / अनाज","Vegetable / सब्जी"])
    print(f"Recommended next crop: {recommended} / अगली फसल के लिए सुझाव: {recommended}")

# 7️⃣ Pest & Disease Guide
def pest_disease_guide():
    print("\n🦠 Pest & Disease Guide / कीट और रोग मार्गदर्शिका 🦠")
    print("Theory / सिद्धांत: Helps detect pests early and choose treatment. / जल्दी कीट पहचान में मदद और उपचार का चयन।")
    pest_found = random.choice([True, False])
    if pest_found:
        pest_name = random.choice(["Aphids / एफिड्स","Whitefly / व्हाइटफ्लाई","Locust / टिड्डी"])
        print(f"⚠️ Pest detected: {pest_name}")
    else:
        print("✅ No pests detected / कोई कीट नहीं मिला")

# 8️⃣ Organic Tips
def organic_tips():
    print("\n🌱 Organic Farming Tips / जैविक खेती सुझाव 🌱")
    print("Theory / सिद्धांत: Promotes natural farming methods. / प्राकृतिक खेती के तरीकों को बढ़ावा देता है।")
    tip = random.choice([
        "Use compost instead of chemical fertilizer / रासायनिक उर्वरक की जगह कम्पोस्ट का प्रयोग करें",
        "Mulching helps retain soil moisture / मल्चिंग से मिट्टी में नमी बनी रहती है",
        "Rotate crops to maintain soil fertility / मिट्टी की उर्वरता बनाए रखने के लिए फसल चक्रीकरण करें"
    ])
    print(f"Tip: {tip}")

# 9️⃣ AI Farming Tips
def ai_farming_tips():
    print("\n🤖 AI Farming Tips / AI खेती सुझाव 🤖")
    print("Theory / सिद्धांत: Uses AI to optimize crop growth and market insights. / AI का उपयोग करके फसल वृद्धि और बाजार जानकारी को बेहतर बनाता है।")
    tip = random.choice([
        "Use drone imagery to monitor crop health / ड्रोन इमेजरी से फसल स्वास्थ्य मॉनिटर करें",
        "AI can predict market price trends / AI बाजार मूल्य रुझान पूर्वानुमान कर सकता है",
        "Smart irrigation based on soil sensors / मिट्टी सेंसर आधारित स्मार्ट सिंचाई"
    ])
    print(f"Tip: {tip}")

# 🔟 Crop Insurance Guide
def crop_insurance_guide():
    print("\n📋 Crop Insurance Guide / फसल बीमा मार्गदर्शिका 📋")
    print("Theory / सिद्धांत: Suggests proper insurance for crop safety. / फसल सुरक्षा के लिए उचित बीमा योजना सुझाता है।")
    crop = input("Enter crop name / फसल का नाम: ")
    print(f"Recommended insurance plan for {crop} / {crop} के लिए बीमा योजना सुझाव: Standard Plan / स्टैंडर्ड योजना")

# ---------- ADD TO CATEGORY 1 ----------
categories["1"]["tools"].extend([
    crop_planner,
    soil_health_check,
    fertilizer_calculator,
    seed_calculator,
    irrigation_scheduler,
    crop_rotation,
    pest_disease_guide,
    organic_tips,
    ai_farming_tips,
    crop_insurance_guide
])
import random

# ==============================
# 💧 CATEGORY 2 – Irrigation Management
# ==============================

# 1️⃣ Water Requirement Calculator
def water_schedule_planner():
    print("\n💧 Water Requirement Planner / पानी आवश्यकता योजना")
    print("Theory: Calculates water needed based on area.")
    area = float(input("Enter field area (acres): "))
    water = round(area * random.uniform(1200, 1800), 2)
    print(f"Required Water: {water} Liters")
    print(f"आवश्यक पानी: {water} लीटर")


# 2️⃣ Drip Irrigation Advisor
def drip_irrigation_advisor():
    print("\n🚿 Drip Irrigation Advisor / ड्रिप सिंचाई सलाह")
    print("Theory: Suggests if drip system is suitable.")
    soil = input("Enter soil type (sandy/clay/loamy): ")
    if soil.lower() == "sandy":
        print("Recommended: YES — drip saves water")
    else:
        print("Recommended: Optional use")


# 3️⃣ Sprinkler Scheduler
def sprinkler_scheduler():
    print("\n🌧 Sprinkler Scheduler / स्प्रिंकलर समय योजना")
    days = random.choice(["Every 2 days", "Every 3 days", "Weekly"])
    print(f"Recommended Schedule: {days}")
    print(f"अनुशंसित समय: {days}")


# 4️⃣ Soil Moisture Sensor Simulator
def soil_moisture_sensor():
    print("\n🌱 Soil Moisture Monitor / मिट्टी नमी मॉनिटर")
    moisture = random.randint(10, 90)
    print(f"Soil Moisture Level: {moisture}%")
    print(f"मिट्टी नमी स्तर: {moisture}%")
    if moisture < 30:
        print("⚠ Irrigation needed immediately")


# 5️⃣ Irrigation Cost Calculator
def irrigation_cost_calculator():
    print("\n💰 Irrigation Cost Calculator / सिंचाई लागत कैलकुलेटर")
    hours = float(input("Enter pump hours: "))
    cost = hours * 50
    print(f"Estimated Cost: ₹{cost}")
    print(f"अनुमानित लागत: ₹{cost}")


# 6️⃣ Rainwater Harvest Tracker
def rainwater_harvest_tracker():
    print("\n🌧 Rainwater Storage Tracker")
    rainfall = float(input("Enter rainfall (mm): "))
    stored = rainfall * 100
    print(f"Stored Water: {stored} liters")
    print(f"संग्रहित पानी: {stored} लीटर")


# 7️⃣ AI Irrigation Predictor
def ai_irrigation_predictor():
    print("\n🤖 AI Irrigation Predictor")
    weather = random.choice(["Hot", "Normal", "Rainy"])
    print(f"Weather Prediction: {weather}")
    if weather == "Hot":
        print("Increase irrigation frequency")
    else:
        print("Normal irrigation sufficient")


# 8️⃣ Drip System Monitor
def drip_system_monitor():
    print("\n🔧 Drip System Health Check")
    status = random.choice(["Working Fine", "Clogged Pipes", "Leak Detected"])
    print(f"System Status: {status}")


# 9️⃣ Irrigation Efficiency Checker
def irrigation_efficiency_checker():
    print("\n📊 Irrigation Efficiency Checker")
    efficiency = random.randint(50, 95)
    print(f"Efficiency: {efficiency}%")
    if efficiency < 70:
        print("⚠ Improve irrigation system")


# 🔟 Water Saving Tips Generator
def water_saving_tips():
    print("\n💡 Water Saving Tips")
    tips = [
        "Use drip irrigation",
        "Irrigate during early morning",
        "Use mulching to retain moisture",
        "Avoid overwatering"
    ]
    print(random.choice(tips))


# ==============================
# ADD TO CATEGORY 2
# ==============================

categories["2"]["tools"].extend([
    water_schedule_planner,
    drip_irrigation_advisor,
    sprinkler_scheduler,
    soil_moisture_sensor,
    irrigation_cost_calculator,
    rainwater_harvest_tracker,
    ai_irrigation_predictor,
    drip_system_monitor,
    irrigation_efficiency_checker,
    water_saving_tips
])
import random

# ==============================
# 🦠 CATEGORY 3 – Pest & Disease Control
# ==============================

# 1️⃣ Pest Identification Tool
def pest_identification_tool():
    print("\n🐛 Pest Identification Tool / कीट पहचान टूल")
    print("Detects common pests based on symptoms.")
    symptom = input("Enter symptom (holes/yellow leaves/spots): ")
    pests = {
        "holes": "Caterpillar / इल्ली",
        "yellow": "Aphids / एफिड्स",
        "spots": "Fungal infection / फंगल रोग"
    }
    print("Detected:", pests.get(symptom.lower(), "Unknown"))


# 2️⃣ Disease Detection Tool
def disease_identification_tool():
    print("\n🦠 Disease Detection Tool")
    moisture = int(input("Enter soil moisture %: "))
    if moisture > 70:
        print("⚠ High chance of fungal disease")
    else:
        print("Low disease risk")


# 3️⃣ Pesticide Recommendation Tool
def pesticide_recommendation_tool():
    print("\n💊 Pesticide Recommendation")
    pest = input("Enter pest name: ")
    print(f"Recommended pesticide for {pest}: Neem Oil Spray")


# 4️⃣ Disease Alert Generator
def disease_alerts():
    print("\n🚨 Disease Alert System")
    humidity = random.randint(40, 95)
    print("Humidity:", humidity, "%")
    if humidity > 80:
        print("⚠ Disease Risk HIGH")


# 5️⃣ Treatment Scheduler
def treatment_scheduler():
    print("\n📅 Treatment Scheduler")
    days = random.choice([5, 7, 10])
    print(f"Apply treatment every {days} days")


# 6️⃣ Pest Trend Analyzer
def pest_trend_analyzer():
    print("\n📊 Pest Trend Analyzer")
    infestation = random.randint(10, 90)
    print("Pest Level:", infestation, "%")
    if infestation > 60:
        print("⚠ Immediate control required")


# 7️⃣ Organic Pest Control Guide
def organic_pest_control_guide():
    print("\n🌿 Organic Pest Control Tips")
    tips = [
        "Use Neem Oil Spray",
        "Release ladybugs",
        "Use garlic spray",
        "Apply cow urine solution"
    ]
    print(random.choice(tips))


# 8️⃣ AI Disease Predictor
def ai_disease_predictor():
    print("\n🤖 AI Disease Predictor")
    weather = random.choice(["Hot", "Humid", "Dry"])
    print("Weather:", weather)
    if weather == "Humid":
        print("⚠ Fungal disease risk HIGH")


# 9️⃣ Pest Control Cost Calculator
def pest_control_cost_calculator():
    print("\n💰 Pest Control Cost Calculator")
    area = float(input("Enter area (acres): "))
    cost = area * 300
    print(f"Estimated Cost: ₹{cost}")


# 🔟 Market Price Checker (Pesticides)
def pest_control_market_prices():
    print("\n🏪 Pesticide Market Prices")
    products = ["Neem Oil ₹250", "Insecticide ₹600", "Fungicide ₹450"]
    print(random.choice(products))


# ==============================
# ADD TO CATEGORY 3
# ==============================

categories["3"]["tools"].extend([
    pest_identification_tool,
    disease_identification_tool,
    pesticide_recommendation_tool,
    disease_alerts,
    treatment_scheduler,
    pest_trend_analyzer,
    organic_pest_control_guide,
    ai_disease_predictor,
    pest_control_cost_calculator,
    pest_control_market_prices
])
# ---------- MENU LOOP ----------
while True:
    print("\n===== PARTH'S APP =====")
    for key, val in categories.items():
        print(f"{key}. {val['name']}")
    print("0. ❌ Exit / बाहर")

    cat_choice = input("Choose Category / कैटेगरी चुनें: ").strip()
    if cat_choice=="0":
        show_msg("🙏 धन्यवाद!", "🙏 Thank You!")
        break
    elif cat_choice in categories:
        cat = categories[cat_choice]
        if not cat["tools"]:
            show_msg("⚠️ कोई टूल अभी नहीं है।", "⚠️ No tools available yet.")
            continue
        print(f"\n===== {cat['name']} =====")
        for i, tool in enumerate(cat["tools"],1):
            print(f"{i}. {tool.__name__.replace('_',' ').title()}")
        print("0. 🔙 Back / पीछे")
        while True:
            try:
                choice = int(input("Choose Tool / टूल चुनें: "))
                if choice==0: break
                elif 1<=choice<=len(cat["tools"]):
                    cat["tools"][choice-1]()
                else:
                    show_msg("❌ Invalid Choice / विकल्प गलत है।", "❌ Invalid Choice")
            except:
                show_msg("❌ Invalid input / संख्या सही नहीं।", "❌ Invalid input")
    else:
        show_msg("❌ Invalid Choice / विकल्प गलत है।", "❌ Invalid Choice")