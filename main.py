import argparse
from text_analyzer import TextAnalyzer


def main():
    parser = argparse.ArgumentParser(description="TextPulse: CLI Text Statistics & Formatting Utility")
    parser.add_argument("text", type=str, help="The input text string to analyze or transform.")

    parser.add_argument("--case", choices=["snake", "camel", "pascal", "kebab", "title"], help="Convert text to a specific case style")
    parser.add_argument("--freq", action="store_true", help="Display keyword frequency analysis")

    args = parser.parse_args()
    analyzer = TextAnalyzer(args.text)

    print("\n" + "="*40)
    print("⚡TEXTPULSE REPORT ⚡")
    print("="*40)
    print(f"Input Text  :{args.text}")
    print(f"Word Count  :{analyzer.word_count()}")
    print(f"Char Count  :{analyzer.char_count(include_spaces=True)} (with spaces)")
    print(f"Reading Time :{analyzer.reading_time()} minutes")

    if args.case:
        try:
            transformed = analyzer.convert_case(args.case)
            print(f"Case ({args.case}) : {transformed}")
        except ValueError as e:
            print(f"Error     :{e}")
    if args.freq:
        print("\nTop Keywords:")
        top_words = analyzer.keyword_frequency()
        if top_words:
            for word, count in top_words:
                bar = "█" * count
                print(f"{word:<10} | {count} {bar}")
        else:
            print("  NO significant keywords found.")
    print("="*40 + "\n")
if __name__ == "__main__":
    main()



