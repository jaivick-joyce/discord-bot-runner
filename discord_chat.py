import time
import random
import requests

# ⚠️ APNE TOKENS UPDATE KARLENA PASSWORDS RESET KARKE!
USER_TOKENS = [
    "MTUwNDAzMzk2NTAxMzYwMjQ0MA.GDsybc.UfkrUXr2d_aZw0NAV79_Z5VaCbJigmO_NwKFys",
    "MTQ2ODMwNzk0MDc0OTM0NDgxMQ.GS2B5P.7wRxQYarssK37U0Gy4TvRLrV_wAgJAFRnD94Tg",
    "OTcwNjAwMTUxMzM5MTI2Nzg1.GDJkOB.YfAKLfc_emeQrHgPx0ifnXn40pO4E1x0AS2vXk"
]

CHANNEL_ID = "1356668062945902733"
API_URL = f"https://discord.com/api/v10/channels/{CHANNEL_ID}/messages"

base_conversation = [
    {"user_idx": 1, "text": "abey ruko ek minute, sach me ja rha tha par ek meme dikha"},
    {"user_idx": 0, "text": "chal shuru ho gya iska insta gyan"},
    {"user_idx": 2, "text": "bhej bhej group pe bhej idhar mat daal link"},
    {"user_idx": 1, "text": "arre idhar hi suno, bol rha h ki coding seekho lmfao"},
    {"user_idx": 0, "text": "bhai coding se yaad aaya kisi ne vo ai tools chala ke dekhe?"},
    {"user_idx": 2, "text": "haan bhai dimag kharab kar rha h vo toh alag hi chal rha"},
    {"user_idx": 1, "text": "mere se toh hello world ka program ni banta sahi se"},
    {"user_idx": 0, "text": "vahi toh, hum log bas scroll karne ke liye bane hain"},
    {"user_idx": 2, "text": "wese tum dono ne vo nayi movie dekhi kya?"},
    {"user_idx": 1, "text": "kaunsi? vo jo abhi theatres me chal rhi?"},
    {"user_idx": 0, "text": "paisa lagta h bhai theatre me, ott pe aane do"},
    {"user_idx": 2, "text": "abey telegram zindabad, kaun wait karega ek mahina"},
    {"user_idx": 1, "text": "print quality bekar hoti h yar maza ni aata"},
    {"user_idx": 0, "text": "toh tu kharid le netflix ka subscription, bada ameer h na"},
    {"user_idx": 2, "text": "haha iske paas khud ka prime chalane ka paisa ni h"},
    {"user_idx": 1, "text": "shant ho jao bhaiyo, dost ka account udhaar le rakha h maine"},
    {"user_idx": 0, "text": "vahi mai sochu, chal ye batao shaam ko gaming ka kya scene?"},
    {"user_idx": 2, "text": "bgmi khelenge? mai toh taiyar hu ekdum"},
    {"user_idx": 1, "text": "mera ping high aata h humesha hotspot se khelta hu na"},
    {"user_idx": 0, "text": "bhai tera net humesha rotu hi rehta h kab se bol rha wifi lagwa le"},
    {"user_idx": 2, "text": "wifi ke liye ghar wale bolte h pehle padhai karo"},
    {"user_idx": 1, "text": "padhai se yaad aaya kal ka assignment kiya kisi ne?"},
    {"user_idx": 0, "text": "assignment? kaunsa assignment bhai? darna mat ab"},
    {"user_idx": 2, "text": "vahi jo pdf aayi thi group me 20 page ki"},
    {"user_idx": 1, "text": "maine toh touch bhi nhi kiya abhi tak"},
    {"user_idx": 0, "text": "choddo kal subah subah kisi toppers se mangenge"},
    {"user_idx": 2, "text": "topper log bhav dete hain kya aajkal?"},
    {"user_idx": 1, "text": "bhai thodi tareef kardo ek minute me screen shot bhejte hain"},
    {"user_idx": 0, "text": "sahi jugad h tera vaise bhot tez ho rhe ho"},
    {"user_idx": 2, "text": "acha chlo ek serious baat batao"},
    {"user_idx": 1, "text": "kya hua? sab khairiyat?"},
    {"user_idx": 0, "text": "bol bol kya baat h"},
    {"user_idx": 2, "text": "kya aapke toothpaste me namak hai?"},
    {"user_idx": 1, "text": "abe yaar fir se vahi bakwaas meme 🤦‍♂️"},
    {"user_idx": 0, "text": "mai toh bol rha hu iska toothpaste hi chura lo"},
    {"user_idx": 2, "text": "hahaha bina namak wala dunga isko"},
    {"user_idx": 1, "text": "tum dono milke meri ragging lena bas"},
    {"user_idx": 0, "text": "gussa mat ho bhai, tere ko momos khilayenge delhi aake"},
    {"user_idx": 2, "text": "ha mai isko lekar aunga dukaan pe"},
    {"user_idx": 1, "text": "theek h par paise tum dono doge, mai phuti kaudi ni nikalunga"},
    {"user_idx": 0, "text": "wese tumhari gully me price kya h momos ka?"},
    {"user_idx": 2, "text": "idhar 30 ke half milte hain badhiya wale"},
    {"user_idx": 1, "text": "bengaluru me toh 60-70 ke bina baat ni banti"},
    {"user_idx": 0, "text": "mumbai me toh momos milte hi bekar hain, vada pav hi king h"},
    {"user_idx": 2, "text": "vada pav me kya h bas pav me aloo daal dete hain"},
    {"user_idx": 1, "text": "vahi toh, thoda mirchi laga ke bas bechte rhte hain"},
    {"user_idx": 0, "text": "abe tameez se baat karo, emotion h humara vo"},
    {"user_idx": 2, "text": "acha sorry gussa mat ho khao apna aloo bonda pav"},
    {"user_idx": 1, "text": "hahaha aloo bonda bol diya bhyi"},
    {"user_idx": 0, "text": "tum dono ka din kharab lag rha h mere hatho"},
    {"user_idx": 2, "text": "accha ye btao garmi kaisi h udhar?"},
    {"user_idx": 1, "text": "idhar toh ac chalana pad rha h din me"},
    {"user_idx": 0, "text": "hum toh cooler ke samne bethe rehte hain pure din"},
    {"user_idx": 2, "text": "cooler ki awaz me neend badhiya aati h vaise"}
]

# Generate 90 messages per account (270 total lines)
conversation = []
while len(conversation) < 270:
    for line in base_conversation:
        loop_count = (len(conversation) // len(base_conversation)) + 1
        text_modifier = f" (part {loop_count})" if loop_count > 1 else ""
        
        conversation.append({
            "user_idx": line["user_idx"],
            "text": f"{line['text']}{text_modifier}"
        })
        if len(conversation) == 270:
            break

def run_self_bots():
    last_sent_time = {i: 0.0 for i in range(len(USER_TOKENS))}
    msg_counters = {i: 0 for i in range(len(USER_TOKENS))}
    last_message_id = None
    
    print(f"Total lines scheduled to transfer: {len(conversation)}")
    print("Tip: Message ke baad 'p' likh kar Enter dabane se script pause ho jayegi.\n")
    
    for i, line in enumerate(conversation):
        idx = line["user_idx"]
        token = USER_TOKENS[idx]
        
        # 1. Slowmode Safeguard (Minimum 10.5 seconds check)
        time_since_last_message = time.time() - last_sent_time[idx]
        if time_since_last_message < 10.5:
            sleep_needed = 10.5 - time_since_last_message
            print(f"[Line {i+1}] Account {idx} cooling down. Waiting {sleep_needed:.2f}s...")
            time.sleep(sleep_needed)
            
        headers = {
            "Authorization": token,
            "Content-Type": "application/json",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"
        }
        
        payload = {"content": line["text"]}
        
        # Discord Reply Relation Connection
        if last_message_id:
            payload["message_reference"] = {
                "channel_id": CHANNEL_ID,
                "message_id": last_message_id
            }
        
        # 2. Transmission (Send Message)
        response = requests.post(API_URL, json=payload, headers=headers)
        
        if response.status_code == 200:
            msg_counters[idx] += 1
            current_msg_data = response.json()
            last_message_id = current_msg_data.get("id")
            
            print(f"[Line {i+1}] Account {idx} Replied Successfully ({msg_counters[idx]}/90): \"{line['text']}\"")
            last_sent_time[idx] = time.time()
            # ❌ Delete function ko yahan se poora saaf kar diya hai.
                    
        elif response.status_code == 429:
            retry_after = response.json().get("retry_after", 12)
            print(f"⚠️ Channel Rate limited! Sleeping for {retry_after}s...")
            time.sleep(retry_after)
            last_sent_time[idx] = time.time() 
        elif response.status_code == 401:
            print(f"❌ Critical Error: Token for Account {idx} is invalid!")
            break
        else:
            print(f"Failed to post. Status Code: {response.status_code}")
            
        # 3. INTERACTIVE PAUSING & RANDOM DELAY FEATURE
        # Har message ke baad terminal user input mangega (lekin sirf 0.1s ke liye monitor karega)
        user_choice = input("Press [Enter] to continue or type 'p' to PAUSE: ").strip().lower()
        
        if user_choice == 'p':
            print("\n⏸️  SCRIPT PAUSED. Sabhi bots ruk gaye hain.")
            input("▶️  Dobara start karne ke liye simple [Enter] dabayein...")
            print("Resuming script execution...\n")
        
        # Human Typing Random Variance Delay (7 to 15 seconds)
        random_delay = random.uniform(7.0, 15.0)
        print(f"⌛ Sleeping for a random human delay of {random_delay:.2f} seconds...\n")
        time.sleep(random_delay)
        
    print("\n✅ Challenge complete! All 90 messages per account sent without deletion.")

if __name__ == "__main__":
    print("Starting friendly challenge configuration script... Close window to stop.")
    run_self_bots()
