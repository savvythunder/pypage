from typing import List as ListType, Union, Optional
from .elements import Element

class Row(Element):
    """Bootstrap row component for grid layout"""
    
    def __init__(self, content: Union[str, ListType] = "", css_class: Optional[str] = None,
                 id_attr: Optional[str] = None):
        row_class = "row"
        if css_class:
            row_class += f" {css_class}"
        super().__init__("div", css_class=row_class, id_attr=id_attr)
        
        if isinstance(content, list):
            self.content = ""
            for item in content:
                if hasattr(item, 'render'):
                    self.content += item.render()
                else:
                    self.content += str(item)
        else:
            self.content = str(content)

    def add_column(self, column):
        """Add a column to the row"""
        if hasattr(column, 'render'):
            self.content += column.render()
        else:
            self.content += str(column)
        return self

class Column(Element):
    """Bootstrap column component for grid layout"""
    
    def __init__(self, content: Union[str, ListType] = "", width: Optional[Union[str, int]] = None,
                 css_class: Optional[str] = None, id_attr: Optional[str] = None):
        # Determine column class based on width
        if width is None:
            col_class = "col"
        elif isinstance(width, int):
            col_class = f"col-{width}"
        else:
            col_class = f"col-{width}"
            
        if css_class:
            col_class += f" {css_class}"
        
        super().__init__("div", css_class=col_class, id_attr=id_attr)
        
        if isinstance(content, list):
            self.content = ""
            for item in content:
                if hasattr(item, 'render'):
                    self.content += item.render()
                else:
                    self.content += str(item)
        else:
            self.content = str(content)

    def add_content(self, content):
        """Add content to the column"""
        if hasattr(content, 'render'):
            self.content += content.render()
        else:
            self.content += str(content)
        return self

class Flex(Element):
    """Flexbox container component"""
    
    def __init__(self, content: Union[str, ListType] = "", direction: str = "row",
                 justify: Optional[str] = None, align: Optional[str] = None,
                 wrap: bool = False, css_class: Optional[str] = None,
                 id_attr: Optional[str] = None):
        flex_class = "d-flex"
        
        # Direction
        if direction == "column":
            flex_class += " flex-column"
        elif direction == "row-reverse":
            flex_class += " flex-row-reverse"
        elif direction == "column-reverse":
            flex_class += " flex-column-reverse"
        
        # Justify content
        if justify:
            justify_class_map = {
                "start": "justify-content-start",
                "end": "justify-content-end",
                "center": "justify-content-center",
                "between": "justify-content-between",
                "around": "justify-content-around",
                "evenly": "justify-content-evenly"
            }
            if justify in justify_class_map:
                flex_class += f" {justify_class_map[justify]}"
        
        # Align items
        if align:
            align_class_map = {
                "start": "align-items-start",
                "end": "align-items-end",
                "center": "align-items-center",
                "baseline": "align-items-baseline",
                "stretch": "align-items-stretch"
            }
            if align in align_class_map:
                flex_class += f" {align_class_map[align]}"
        
        # Wrap
        if wrap:
            flex_class += " flex-wrap"
        
        if css_class:
            flex_class += f" {css_class}"
        
        super().__init__("div", css_class=flex_class, id_attr=id_attr)
        
        if isinstance(content, list):
            self.content = ""
            for item in content:
                if hasattr(item, 'render'):
                    self.content += item.render()
                else:
                    self.content += str(item)
        else:
            self.content = str(content)

    def add_item(self, item):
        """Add an item to the flex container"""
        if hasattr(item, 'render'):
            self.content += item.render()
        else:
            self.content += str(item)
        return self