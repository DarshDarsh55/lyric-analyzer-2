#!/usr/bin/env python3
"""
Chat Logger for Lyric Analyzer 2 Project
Saves important conversations and decisions
"""

import os
from datetime import datetime

def save_conversation(title, content, conversation_type="general"):
    """
    Save a conversation to the project notes
    
    Args:
        title (str): Descriptive title for the conversation
        content (str): Full conversation content
        conversation_type (str): 'general', 'decision', 'code', 'future'
    """
    
    # Create directory structure if it doesn't exist
    notes_dir = "project_notes"
    convos_dir = os.path.join(notes_dir, "conversations")
    
    os.makedirs(convos_dir, exist_ok=True)
    
    # Generate filename with timestamp
    timestamp = datetime.now().strftime("%Y%m%d_%H%M")
    filename = f"{timestamp}_{conversation_type}_{title.replace(' ', '_')}.md"
    filepath = os.path.join(convos_dir, filename)
    
    # Format content with metadata
    formatted_content = f"""# {title}

**Date:** {datetime.now().strftime("%Y-%m-%d %H:%M:%S")}
**Type:** {conversation_type}
**Status:** Active

---

{content}

---

## Key Takeaways
- [Add bullet points of important decisions/code/ideas]

## Action Items
- [Add next steps]

## Future Considerations
- [Add items for later implementation]
"""
    
    # Save to file
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(formatted_content)
    
    print(f"✅ Conversation saved: {filepath}")
    return filepath

def quick_save_current_chat():
    """
    Quick function to save the current chat context
    Call this function to save whatever conversation you're having
    """
    
    # You'll paste the actual conversation content here
    title = input("Enter chat title (e.g., 'System Architecture Discussion'): ")
    print("\nPaste the conversation content below (Press Ctrl+Z then Enter when done on Windows, or Ctrl+D on Mac/Linux):")
    
    content_lines = []
    try:
        while True:
            line = input()
            content_lines.append(line)
    except EOFError:
        pass
    
    content = "\n".join(content_lines)
    
    # Determine conversation type
    print("\nConversation type:")
    print("1. General discussion")
    print("2. Decision/principle")  
    print("3. Code/technical")
    print("4. Future planning")
    
    type_choice = input("Enter number (1-4): ")
    type_map = {"1": "general", "2": "decision", "3": "code", "4": "future"}
    conv_type = type_map.get(type_choice, "general")
    
    return save_conversation(title, content, conv_type)

if __name__ == "__main__":
    quick_save_current_chat()