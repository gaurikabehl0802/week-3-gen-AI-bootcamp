styles = {

"Anime":
"anime style, vibrant colors, highly detailed",

"Cyberpunk":
"cyberpunk aesthetic, neon lights, futuristic city",

"Realistic":
"photorealistic, 8k quality, highly detailed",

"Fantasy":
"fantasy art, magical atmosphere, cinematic lighting"

}



def build_prompt(user_prompt, style):

    return f"{user_prompt}, {styles[style]}"