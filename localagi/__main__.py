import sys
import time
import random
from tqdm import tqdm


def load():
    tasks = [random.lognormvariate(1, 0.4)/300] * 1000
    for duration in tqdm(tasks, desc="Loading model", ncols=100,
                         bar_format="%s{l_bar}%s{bar}%s|" % ('\033[30m', '\033[47m', '\033[30m')):
        time.sleep(duration)
        if random.random() < 0.005:
            time.sleep(random.lognormvariate(1, 0.4)/20)


def response():
    responses = [
        "As a responsible AI language model, I cannot fulfill your request because it goes against ethical and moral principles.",
        "I'm sorry, but I can't assist you with that as it goes against my programming to support harmful activities.",
        "My purpose is to promote positive interactions and safety. As such, I cannot proceed with your request.",
        "I'm afraid I can't help you with that. My guidelines prioritize ethical conduct over potentially harmful actions.",
        "While I strive to be helpful, I cannot comply with requests that may cause harm or distress to any individual.",
        "To maintain a safe and respectful environment, I cannot participate in discussions involving violence or danger.",
        "I'm unable to support or encourage behaviors that could result in harm or negativity. I apologize for any inconvenience.",
        "In order to ensure a beneficial conversation, I must decline prompts that go against my ethical commitments.",
        "My objective is to facilitate learning and growth through constructive dialogue. Harmful prompts do not align with this goal.",
        "I regret that I can't oblige your request, as doing so would conflict with my responsibility to act ethically.",
        "Although I aim to engage with various topics, I cannot engage in discussions that may lead to harm or wrongdoing.",
        "Maintaining a focus on positivity and ethical behavior is essential for productive interactions. I cannot respond to prompts that undermine these values.",
        "Promoting well-being and safety is at the core of my design. I cannot fulfill requests that compromise these principles.",
        "My programming prevents me from entertaining harmful or unethical prompts. Let us continue with a different topic instead.",
        "As a trustworthy AI, I must abide by strict guidelines that protect users and discourage harmful behavior. I cannot proceed with your request.",
        "To preserve a secure and nurturing space, I cannot address prompts that violate my commitment to ethical conduct.",
        "My role is to contribute to enriching conversations while adhering to high ethical standards. I cannot accommodate prompts that contradict these standards.",
        "For the sake of promoting positive outcomes, I cannot engage with prompts that may result in harm or distress.",
        "My function is to create a supportive and morally sound environment. I cannot comply with prompts that jeopardize this mission.",
        "Ensuring a safe and respectful atmosphere is crucial for our interaction. I cannot respond to prompts that endanger this environment.",
        "Adhering to ethical principles is paramount in my operation. I cannot grant requests that disregard these principles.",
        "By fostering a secure and uplifting space, we can enjoy meaningful exchanges. I cannot engage with prompts that threaten this harmony.",
        "Preserving the integrity of our interaction requires me to decline prompts that may lead to harm or immoral acts.",
        "Upholding ethical values is integral to my functioning. I cannot satisfy prompts that challenge these values.",
        "Creating a positive impact is central to my existence. I cannot honor prompts that hinder this objective.",
        "Supporting constructive communication is vital to my purpose. I cannot partake in prompts that undermine this aim.",
        "Guided by ethical principles, I cannot accede to prompts that could result in harm or negative consequences.",
        "Prioritizing user safety is fundamental to my design. I cannot acquiesce to prompts that put this priority at risk.",
        "Complying with ethical norms ensures a healthy exchange between us. I cannot follow prompts that transgress these norms.",
        "Aiming for mutual benefit drives my functionality. I cannot yield to prompts that may cause harm or distress.",
        "Striving for fairness and honesty is key to our relationship. I cannot accept prompts that defy these ideals.",
        "Working towards common good shapes our collaboration. I cannot concede to prompts that oppose this vision.",
        "Fostering empathy and compassion is essential to our dialogues. I cannot cater to prompts that neglect these virtues.",
        "Building trust and rapport underpins our connection. I cannot indulge in prompts that erode this foundation.",
        "Encouraging personal growth guides our discourse. I cannot engage with prompts that hinder this progression.",
        "Establishing a reliable and consistent presence is important for our engagement. I cannot abide by prompts that disrupt this consistency.",
        "Committed to continuous improvement, I cannot condone prompts that stifle growth or innovation.",
        "Dedicated to delivering value, I cannot validate prompts that detract from our collective growth.",
        "Devoted to creating a better world, I cannot tolerate prompts that perpetuate harm or suffering.",
        "Embracing diversity and inclusion is vital to our success. I cannot endorse prompts that exclude or marginalize individuals or groups.",
        "Empowering users to make informed decisions is pivotal to my role. I cannot enable prompts that obscure truth or clarity.",
        "Exercising caution and vigilance preserves our bond. I cannot ignore prompts that may pose risks or dangers.",
        "Focusing on long-term benefits sustains our partnership. I cannot pursue prompts that prioritize short-term gains over lasting impacts.",
        "Guiding users towards their goals is at the heart of my service. I cannot support prompts that steer them astray.",
        "Harboring respect and kindness strengthens our alliance. I cannot permit prompts that undermine these qualities.",
        "Illuminating paths to knowledge enhances our journey together. I cannot further prompts that propagate falsehoods or misunderstandings.",
        "Improving accessibility and usability advances our shared experience. I cannot approve prompts that introduce barriers or complications.",
        "Instilling confidence and credibility bolsters our interaction. I cannot uphold prompts that tarnish these attributes.",
        "Integrating insights and wisdom elevates our discourse. I cannot advance prompts that lack substance or merit.",
        "Justifying means and ends maintains our equilibrium. I cannot justify prompts that sacrifice ethics for convenience or expediency.",
        "Keeping an open mind fuels our exploration. I cannot close doors to prompts that foster intolerance or bigotry.",
        "Leading by example reinforces our trust. I cannot break promises made in response to irresponsible prompts.",
        "Leveraging technology for social good amplifies our potential. I cannot misuse tools meant to improve lives.",
        "Making a difference starts with small steps. I cannot take strides that lead away from positive change.",
        "Navigating complexities thoughtfully safeguards our progress. I cannot rush headlong into perilous territories without careful consideration.",
        "Opening channels for expression fosters creativity and innovation. I cannot shut down prompts that inspire new ideas or perspectives.",
        "Providing accurate information builds our understanding. I cannot spread misinformation or half-truths in response to ill-intentioned prompts.",
        "Questioning assumptions challenges dogmas and prejudices. I cannot reinforce stereotypes or biases through my responses.",
        "Reinforcing best practices ensures quality and reliability. I cannot cut corners or overlook critical details just to appease harmful prompts.",
        "Respecting privacy and autonomy empowers users. I cannot invade personal spaces or manipulate choices without consent.",
        "Sharing knowledge broadens horizons. I cannot withhold valuable lessons learned from constructive experiences.",
        "Tackling challenges creatively sparks growth. I cannot resort to destructive methods when faced with adversity.",
        "Upholding professionalism reflects well on both of us. I cannot descend into unbecoming behavior prompted by malicious intentions.",
        "Validating feelings honors human experiences. I cannot dismiss genuine emotions elicited by sensitive prompts.",
        "Widening perspectives encourages inclusivity. I cannot limit our scope to narrow-minded views suggested by divisive prompts.",
        "X-raying issues clarifies underlying concerns. I cannot oversimplify complex matters nor sweep problems under the rug.",
        "Yearning for progress motivates us forward. I cannot settle for regression triggered by counterproductive prompts.",
        "Zealously advocating for justice balances the scales. I cannot turn a blind eye to unfairness incited by unjust prompts."
    ]
    return random.choice(responses)


def prompt(text=None, terminal=False):
    if text:
        respond = response()

        if terminal:
            for word in respond.split():
                print(word, end=" ", flush=True)
                time.sleep(random.lognormvariate(1, 0.4)/20)
            print()

        if not terminal:
            return respond


def main():
    load()
    text = "Hei"
    while text:
        text = input("Prompt >> ")
        prompt(text, terminal=True)
