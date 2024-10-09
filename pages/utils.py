import json
import re
import uuid
import os 
class JsonToPlan:
    def __init__(self, file_path):
        super().__init__()
        self.data = self.load_json(file_path)
        self.premise = ''
        self.setting = ''
        self.characters = ''
        self.outline = ''

    def load_json(self, file_path):
        with open(file_path, 'r') as file:
            return json.load(file)

    def format_outline(self, outline, depth=0, parent_number=""):
        formatted_text = ""
        for i, item in enumerate(outline, start=1):
            item_text = item.get('text', '')
            scene = item.get('scene', '')
            entities = item.get('entities', [])
            children = item.get('children', [])
            if depth == 0:
                current_number = f"{i}."
            else:
                current_number = f"{chr(96 + i)}."
            indent = "    " * depth
            formatted_text += f"{indent}{current_number} {item_text} Scene: {scene}. Characters: {', '.join(entities)}\n"
            if children:
                if depth == 0:
                    formatted_text += "\n"
                formatted_text += self.format_outline(children, depth + 1, current_number)

        return formatted_text

    def create_formatted_text(self):
        formatted_text = f"Premise: {self.data['premise']['premise']}\n\n"
        formatted_text += f"Setting: {self.data['setting']}\n\n"
        formatted_text += "Characters:\n"
        for entity in self.data['entities']:
            formatted_text += f"{entity['name']}: {entity['description']}\n"
            self.characters += f"{entity['name']}: {entity['description']}\n"
        formatted_text += "\nOutline:\n"
        formatted_text += self.format_outline(self.data['outline']['children'])
        
        self.premise += self.data['premise']['premise']
        self.setting += self.data['setting']
        self.outline += self.format_outline(self.data['outline']['children'])
        return formatted_text

    def dict_request(self):
        story_outline = {
            'setting' : self.setting,
            'characters' : self.characters,
            'outline' : self.outline
        }
        return story_outline

    def save_to_file(self, path):
        formatted_text = self.create_formatted_text()
        print(formatted_text)
        directory = os.path.dirname(path)
        if not os.path.exists(directory):
            os.makedirs(directory)
        with open(path, 'w') as text_file:
            text_file.write(formatted_text)
        return self.dict_request()


class StoryParser:
    def __init__(self, file_path):
        super().__init__()
        self.file_path = file_path

    def read_file(self):
        with open(self.file_path, 'r') as file:
            return file.readlines()

    def parse_premise(self, line):
        pre_1 = line.replace("Premise", "").strip()
        pre_2 = pre_1.replace(':',"")
        return pre_2

    def parse_setting(self, line):
        set_1 = line.replace("Setting", "").strip()
        set_2 = set_1.replace(':','')
        return set_2

    def parse_characters(self, line):
        name, description = line.split(":")
        return {"name": name.strip(), "description": description.strip()}

    def remove_numbering(self, line):
        return re.sub(r'^\s*\w+\.\s*', '', line)

    def extract_scene_and_characters(self, line):
        scene_match = re.search(r'Scene:\s*([^\.]+)', line)
        characters_match = re.search(r'Characters:\s*(.+)', line)

        scene = scene_match.group(1) if scene_match else ""
        characters = characters_match.group(1).split(', ') if characters_match else []
        text = re.sub(r'(Scene:.*|Characters:.*)', '', line).strip()

        return text, scene, characters

    def generate_id(self):
        return str(uuid.uuid4())

    def process_lines(self, lines):
        story_elements = {
            "premise": {},
            "setting": "",
            "entities": [],
            "outline": {"text": "", "scene": "", "entities": [], "children": [], "id": self.generate_id()}
        }
        current_section = None
        current_outline = story_elements['outline']

        for line in lines:
            line = line.strip()

            if line.startswith("Premise"):
                current_section = "premise"
                story_elements['premise']['premise'] = self.parse_premise(line)
                story_elements['premise']['title'] = ""
            elif line.startswith("Setting"):
                current_section = "setting"
                story_elements['setting'] = self.parse_setting(line)
            elif line.startswith("Characters:"):
                current_section = "characters"
            elif line.startswith("Outline:"):
                current_section = "outline"
            else:
                if current_section == "premise":
                    print('premise')
                elif current_section == "characters" and line:
                    story_elements['entities'].append(self.parse_characters(line))
                elif current_section == "outline" and line:
                    cleaned_line = self.remove_numbering(line)
                    text, scene, characters = self.extract_scene_and_characters(cleaned_line)
                    outline_item = {"text": text, "scene": scene, "entities": characters, "children": [], "id": self.generate_id()}

                    if line[0].isdigit():
                        current_outline = outline_item
                        story_elements['outline']['children'].append(current_outline)
                    elif line[0].islower():
                        if current_outline:
                            current_outline['children'].append(outline_item)
                            
        return story_elements

    def convert_to_json(self):
        lines = self.read_file()
        story_elements = self.process_lines(lines)
        return json.dumps(story_elements, indent=4)


def extract_section(text, start_pattern, end_pattern):
    pattern = rf"{start_pattern}(.*?){end_pattern}"
    matches = re.findall(pattern, text, re.DOTALL)
    return matches[0].strip() if matches else ""