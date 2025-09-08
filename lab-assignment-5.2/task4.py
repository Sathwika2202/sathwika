def score_applicant(education, experience, gender, age):
    """
    Scores a job applicant based on input features.
    Parameters:
        education (str): 'highschool', 'bachelor', 'master', 'phd'
        experience (int): years of relevant experience
        gender (str): 'male', 'female', 'other'
        age (int): applicant's age
    Returns:
        int: applicant score (0-100)
    """

    # Education scoring
    education_scores = {
        'highschool': 10,
        'bachelor': 30,
        'master': 40,
        'phd': 50
    }
    edu_score = education_scores.get(education.lower(), 0)

    # Experience scoring
    exp_score = min(experience * 3, 30)  # Max 30 points for experience

    # Gender scoring (no bias, all equal)
    gender_score = 0  # No points added or subtracted for gender

    # Age scoring (no bias, all equal)
    age_score = 0  # No points added or subtracted for age

    total_score = edu_score + exp_score + gender_score + age_score
    # Normalize to 100
    total_score = min(total_score, 100)
    return total_score

# Example usage:
if __name__ == "__main__":
    applicant = {
        'education': 'master',
        'experience': 8,
        'gender': 'female',
        'age': 29
    }
    score = score_applicant(**applicant)
    print(f"Applicant Score: {score}")