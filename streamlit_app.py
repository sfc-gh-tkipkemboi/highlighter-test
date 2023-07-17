import streamlit as st
import pandas as pd
import re

def main():
    # Sample data
    data = {
        'Title': ['Article 1', 'Article 2', 'Article 3', 'Article 4'],
        'Content': [
            'The stock market experienced a downturn today.',
            'The housing market is booming.',
            'Investors are uncertain about the future of the company.',
            'The tech Market is thriving amidst the pandemic.'
        ]
    }
    df = pd.DataFrame(data)
    st.title('Table with Highlighted Term')
    # Display the table with highlighting
    def highlight_market(cell):
        def repl(match):
            return '<span style="color: red;">{}</span>'.format(match.group())
        cell = re.sub(r'\bmarket\b', repl, cell, flags=re.I)
        return cell
    df['Content'] = df['Content'].apply(highlight_market)
    st.markdown(df.to_html(escape=False), unsafe_allow_html=True)

    # Full code
    st.code("""
            import streamlit as st
            import pandas as pd
            import re

            def main():
                # Sample data
                data = {
                    'Title': ['Article 1', 'Article 2', 'Article 3', 'Article 4'],
                    'Content': [
                        'The stock market experienced a downturn today.',
                        'The housing market is booming.',
                        'Investors are uncertain about the future of the company.',
                        'The tech Market is thriving amidst the pandemic.'
                    ]
                }
                df = pd.DataFrame(data)
                st.title('Table with Highlighted Term')
                # Display the table with highlighting
                def highlight_market(cell):
                    def repl(match):
                        return '<span style="color: red;">{}</span>'.format(match.group())
                    cell = re.sub(r'\bmarket\b', repl, cell, flags=re.I)
                    return cell
                df['Content'] = df['Content'].apply(highlight_market)
                st.markdown(df.to_html(escape=False), unsafe_allow_html=True)

            if __name__ == '__main__':
                main()
            """)

if __name__ == '__main__':
    main()
