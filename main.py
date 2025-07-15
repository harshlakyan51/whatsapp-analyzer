import streamlit as st
import preprocessor, helper
import matplotlib.pyplot as plt
import seaborn as sns

st.sidebar.title("📊 WhatsApp Chat Analyzer")

uploaded_file = st.sidebar.file_uploader("📁 Upload your chat file (.txt)")
if uploaded_file is not None:
    bytes_data = uploaded_file.getvalue()
    data = bytes_data.decode("utf-8")
    df = preprocessor.preprocess(data)

    user_list = df['user'].unique().tolist()
    if 'group_notification' in user_list:
        user_list.remove('group_notification')
    user_list.sort()
    user_list.insert(0, "Overall")

    selected_user = st.sidebar.selectbox("🔍 Select user for analysis", user_list)

    if st.sidebar.button("Show Analysis"):

        # ---- Top Stats ----
        num_messages, words, num_media_messages, num_links = helper.fetch_stats(selected_user, df)
        st.title("📈 Top Statistics")
        col1, col2, col3, col4 = st.columns(4)

        with col1:
            st.metric("Total Messages", num_messages)
        with col2:
            st.metric("Total Words", words)
        with col3:
            st.metric("Media Shared", num_media_messages)
        with col4:
            st.metric("Links Shared", num_links)

        # ---- Monthly Timeline ----
        st.title("🗓 Monthly Activity")
        timeline = helper.monthly_timeline(selected_user, df)
        fig, ax = plt.subplots()
        ax.plot(timeline['time'], timeline['message'], color='green', marker='o')
        ax.set_title('Messages per Month')
        ax.set_xlabel('Month-Year')
        ax.set_ylabel('Number of Messages')
        plt.xticks(rotation=45)
        st.pyplot(fig)

        # ---- Daily Timeline ----
        st.title("📅 Daily Activity")
        daily_timeline = helper.daily_timeline(selected_user, df)
        fig, ax = plt.subplots()
        ax.plot(daily_timeline['only_date'], daily_timeline['message'], color='black', marker='o')
        ax.set_title('Messages per Day')
        ax.set_xlabel('Date')
        ax.set_ylabel('Number of Messages')
        plt.xticks(rotation=45)
        st.pyplot(fig)

        # ---- Activity Map ----
        st.title('📊 Weekly & Monthly Activity Map')
        col1, col2 = st.columns(2)

        with col1:
            st.subheader("Busy Days")
            busy_day = helper.week_activity_map(selected_user, df)
            fig, ax = plt.subplots()
            ax.bar(busy_day.index, busy_day.values, color='purple')
            ax.set_title("Messages by Day of Week")
            ax.set_xlabel("Day")
            ax.set_ylabel("Messages")
            plt.xticks(rotation=45)
            st.pyplot(fig)

        with col2:
            st.subheader("Busy Months")
            busy_month = helper.month_activity_map(selected_user, df)
            fig, ax = plt.subplots()
            ax.bar(busy_month.index, busy_month.values, color='orange')
            ax.set_title("Messages by Month")
            ax.set_xlabel("Month")
            ax.set_ylabel("Messages")
            plt.xticks(rotation=45)
            st.pyplot(fig)

        # ---- Heatmap ----
        st.title("🧭 Weekly Activity Heatmap")
        user_heatmap = helper.activity_heatmap(selected_user, df)
        fig, ax = plt.subplots(figsize=(12, 6))
        sns.heatmap(user_heatmap, ax=ax, cmap="YlGnBu")
        ax.set_title("Activity Heatmap (Day vs Hour Slot)")
        st.pyplot(fig)

        # ---- Most Busy Users ----
        if selected_user == 'Overall':
            st.title('🙋 Most Active Users')
            x, new_df = helper.most_busy_users(df)
            col1, col2 = st.columns(2)

            with col1:
                fig, ax = plt.subplots()
                ax.bar(x.index, x.values, color='red')
                ax.set_title("Top 5 Active Users")
                ax.set_ylabel("Message Count")
                plt.xticks(rotation=45)
                st.pyplot(fig)

            with col2:
                st.subheader("User Activity (%)")
                st.dataframe(new_df)

        # ---- WordCloud ----
        st.title("☁️ Word Cloud")
        df_wc = helper.create_wordcloud(selected_user, df)
        fig, ax = plt.subplots()
        ax.imshow(df_wc, interpolation="bilinear")
        ax.axis("off")
        st.pyplot(fig)

        # ---- Most Common Words ----
        st.title("🔤 Most Common Words")
        most_common_df = helper.most_common_words(selected_user, df)
        fig, ax = plt.subplots()
        ax.barh(most_common_df[0], most_common_df[1], color='teal')
        ax.set_xlabel("Frequency")
        ax.set_title("Top 20 Most Used Words")
        plt.xticks(rotation=45)
        st.pyplot(fig)

        # ---- Emoji Analysis ----
        st.title("😀 Emoji Usage Analysis")
        emoji_df = helper.emoji_helper(selected_user, df)
        col1, col2 = st.columns(2)

        with col1:
            st.subheader("Top Emojis")
            emoji_df.columns = ['Emoji', 'Count']
            emoji_df = emoji_df.reset_index(drop=True)
            emoji_df.index += 1
            emoji_df.index.name = "Rank"
            st.dataframe(emoji_df)

        with col2:
            fig, ax = plt.subplots()
            ax.pie(emoji_df["Count"].head(5), labels=emoji_df["Emoji"].head(5), autopct="%0.2f%%", startangle=90)
            ax.set_title("Top 5 Emojis Usage Share")
            st.pyplot(fig)
