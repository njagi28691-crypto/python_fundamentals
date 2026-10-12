import re
from collections import Counter


class TextAnalyzer:
    def __init__(self, text: str):
        self.text = text

    def word_count(self) -> int:
        """Returns total word count."""
        return len(self.text.split())
    
    def char_count(self, include_spaces: bool = True)-> int:
        """Returns character count with or without spaces. """
        if include_spaces:
            return len(self.text)
        return len(self.text.replace(" ",""))
    
    def reading_time(self ,wpm: int = 200)->float:
        """Estimates reading time in minutes based on average WPM."""
        word = self.word_count()
        return round(word / wpm,2)

    def convert_case(self, style: str) -> str:
      """Converts strings into various programming and title cases."""
      words = re.findall(r'[a-zA-Z0-9]+' , self.text)
      if not words:
         return ""

      if style == "snake":
          return "_".join(w.lower() for w in words)
      elif style == "camel":
          return words[0].lower() + "".join(w.capitalize() for w in words[1:])
      elif style == "pascal":
          return "".join(w.capitalize() for w in words)
      elif style == "kebab":
          return "-".join(w.lower() for w in words)
      elif style == "title":
          return self.text.title()
      else:
        raise ValueError(f"Unknown case style ; {style}")
    def keyword_frequency(self, top_n: int = 5) -> list:
        """Finds the most frequent significant words (ignoring common stop words)."""
        stop_words = {
            "the", "a", "an", "and", "or", "but", "in", "on", "at", "to", "for", "of", "with", "by" "is", "from","this", "that","it"
        }
        words = re.findall(r'\b[a-z]{3,}\b', self.text.lower())
        filtered_words = [w for w in words if w not in stop_words]

        return Counter(filtered_words).most_common(top_n)
    
      

                         
        
    
    

  
