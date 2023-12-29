from robot_hat import TTS


if __name__ == "__main__":
    words = ["Hi My name is sunil"]
    tts_robot = TTS()
    for i in words:
        print(i)
        tts_robot.say(i)
        
