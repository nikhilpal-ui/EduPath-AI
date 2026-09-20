import { useMemo, useState } from "react";
import "./App.css";

const API = "http://127.0.0.1:8000";

const KNOWN_SKILLS = [
  "Python",
  "Pandas",
  "NumPy",
  "Matplotlib",
  "Seaborn",
  "SQL",
  "MySQL",
  "Power BI",
  "DAX",
  "Power Query",
  "Excel",
  "Machine Learning",
  "Scikit-learn",
  "Data Cleaning",
  "EDA",
  "Exploratory Data Analysis",
  "Feature Engineering",
  "Data Visualization",
  "Git",
  "GitHub",
  "HTML",
  "CSS",
  "JavaScript",
  "React",
  "Statistics",
  "Deep Learning",
  "NLP",
  "TensorFlow",
  "PyTorch",
  "Docker",
  "REST API",
  "FastAPI",
  "Cloud Computing",
];

const ROLE_OPTIONS = [
  "Data Scientist",
  "Data Analyst",
  "ML Engineer",
  "Frontend Developer",
  "Backend Developer",
];

function App() {
  const [resume, setResume] = useState(null);
  const [role, setRole] = useState("Data Scientist");

  const [skills, setSkills] = useState([]);
  const [skillGap, setSkillGap] = useState(null);
  const [roadmap, setRoadmap] = useState(null);
  const [practice, setPractice] = useState(null);
  const [adaptive, setAdaptive] = useState(null);
  const [progressReport, setProgressReport] = useState(null);

  const [profile, setProfile] = useState({
    name: "",
    email: "",
    experience_level: "Beginner",
    career_goal: "",
    study_hours: 10,
  });

  const [portfolio, setPortfolio] = useState({
    url: "",
    description: "",
  });

  const [certificates, setCertificates] = useState([]);

  const [projects, setProjects] = useState([
    {
      title: "",
      description: "",
      technologies: "",
    },
  ]);

  const [activities, setActivities] = useState([]);

  const [qaQuestion, setQaQuestion] = useState("");
  const [qaAnswer, setQaAnswer] = useState(null);

  const [loading, setLoading] = useState(false);
  const [analysisComplete, setAnalysisComplete] = useState(false);
  const [errorMessage, setErrorMessage] = useState("");

  // -----------------------------
  // CERTIFICATES
  // -----------------------------

  const addCertificate = () => {
    setCertificates([
      ...certificates,
      {
        name: "",
        platform: "",
        status: "Completed",
      },
    ]);
  };

  const updateCertificate = (index, field, value) => {
    const updated = [...certificates];

    updated[index] = {
      ...updated[index],
      [field]: value,
    };

    setCertificates(updated);
  };

  const removeCertificate = (index) => {
    setCertificates(
      certificates.filter((_, i) => i !== index)
    );
  };

  // -----------------------------
  // PROJECTS
  // -----------------------------

  const addProject = () => {
    setProjects([
      ...projects,
      {
        title: "",
        description: "",
        technologies: "",
      },
    ]);
  };

  const updateProject = (index, field, value) => {
    const updated = [...projects];

    updated[index] = {
      ...updated[index],
      [field]: value,
    };

    setProjects(updated);
  };

  const removeProject = (index) => {
    if (projects.length === 1) return;

    setProjects(
      projects.filter((_, i) => i !== index)
    );
  };

  // -----------------------------
  // EXTRA SKILL DETECTION
  // -----------------------------

  const extractExtraSkills = () => {
    const source = [
      portfolio.description,
      portfolio.url,

      ...certificates.map(
        (certificate) =>
          `${certificate.name} ${certificate.platform}`
      ),

      ...projects.map(
        (project) =>
          `${project.title} ${project.description} ${project.technologies}`
      ),
    ]
      .join(" ")
      .toLowerCase();

    return KNOWN_SKILLS.filter((skill) =>
      source.includes(skill.toLowerCase())
    );
  };

  const combinedSkills = useMemo(() => {
    return [
      ...new Set([
        ...skills,
        ...extractExtraSkills(),
      ]),
    ];
  }, [
    skills,
    portfolio,
    certificates,
    projects,
  ]);

  // -----------------------------
  // RESUME ANALYSIS
  // -----------------------------

  const uploadResume = async () => {
    if (!resume) {
      alert("Please select a PDF resume first.");
      return;
    }

    setLoading(true);
    setErrorMessage("");

    try {
      // 1. Resume upload
      const formData = new FormData();

      formData.append("file", resume);

      const response = await fetch(
        `${API}/resume/upload`,
        {
          method: "POST",
          body: formData,
        }
      );

      const data = await response.json();

      if (!response.ok) {
        throw new Error(
          data.detail || "Resume upload failed"
        );
      }

      const resumeSkills =
        data.profile?.skills || [];

      // 2. Add portfolio/project/certificate skills
      const extraSkills =
        extractExtraSkills();

      const allSkills = [
        ...new Set([
          ...resumeSkills,
          ...extraSkills,
        ]),
      ];

      setSkills(allSkills);

      // 3. Skill Gap
      const gapResponse = await fetch(
        `${API}/skill-gap/analyze`,
        {
          method: "POST",
          headers: {
            "Content-Type": "application/json",
          },
          body: JSON.stringify({
            current_skills: allSkills,
            target_role: role,
          }),
        }
      );

      const gapData =
        await gapResponse.json();

      if (!gapResponse.ok) {
        throw new Error(
          gapData.detail ||
            "Skill gap analysis failed"
        );
      }

      setSkillGap(gapData);

      // 4. Roadmap
      const roadmapResponse = await fetch(
        `${API}/roadmap/generate`,
        {
          method: "POST",
          headers: {
            "Content-Type": "application/json",
          },
          body: JSON.stringify({
            missing_skills:
              gapData.missing_skills,

            weeks: 4,

            hours_per_week:
              Number(profile.study_hours) || 10,
          }),
        }
      );

      const roadmapData =
        await roadmapResponse.json();

      if (!roadmapResponse.ok) {
        throw new Error(
          roadmapData.detail ||
            "Roadmap generation failed"
        );
      }

      setRoadmap(roadmapData);

      // 5. Practice
      const practiceResponse = await fetch(
        `${API}/practice/generate`,
        {
          method: "POST",
          headers: {
            "Content-Type": "application/json",
          },
          body: JSON.stringify({
            skills: gapData.missing_skills,
            tasks_per_skill: 3,
          }),
        }
      );

      const practiceData =
        await practiceResponse.json();

      if (!practiceResponse.ok) {
        throw new Error(
          practiceData.detail ||
            "Practice generation failed"
        );
      }

      setPractice(practiceData);

      setAdaptive({
        status: "Ready",

        message:
          "Your personalized learning journey has been generated. Complete learning activities to adapt it.",
      });

      setProgressReport(null);

      setAnalysisComplete(true);

      setTimeout(() => {
        document
          .getElementById("skills")
          ?.scrollIntoView({
            behavior: "smooth",
          });
      }, 150);
    } catch (error) {
      console.error(error);

      setErrorMessage(error.message);

      alert(error.message);
    } finally {
      setLoading(false);
    }
  };

  // -----------------------------
  // COMPLETE ACTIVITY
  // -----------------------------

  const completeActivity = async (
    skill,
    score
  ) => {
    const numericScore = Math.max(
      0,
      Math.min(100, Number(score))
    );

    const newActivity = {
      id: `${skill}-${Date.now()}`,

      skill,

      score: numericScore,

      completed: true,

      completedAt:
        new Date().toLocaleString(),
    };

    setActivities((current) => {
      const withoutOld =
        current.filter(
          (item) =>
            item.skill.toLowerCase() !==
            skill.toLowerCase()
        );

      return [
        ...withoutOld,
        newActivity,
      ];
    });

    try {
      const response = await fetch(
        `${API}/adaptive/evaluate`,
        {
          method: "POST",

          headers: {
            "Content-Type":
              "application/json",
          },

          body: JSON.stringify({
            skill,

            score: numericScore,

            completed: true,
          }),
        }
      );

      const data =
        await response.json();

      if (response.ok) {
        setAdaptive(data);
      }
    } catch (error) {
      console.error(error);
    }
  };

  // -----------------------------
  // PROGRESS REPORT
  // -----------------------------

  const generateProgressReport =
    async () => {
      if (!skillGap) {
        alert(
          "Please analyze your profile first."
        );

        return;
      }

      try {
        const requiredSkills =
          skillGap.required_skills || [];

        const progress =
          requiredSkills.map((skill) => {
            const activity =
              activities.find(
                (item) =>
                  item.skill.toLowerCase() ===
                  skill.toLowerCase()
              );

            if (activity) {
              return {
                skill,

                score: activity.score,

                completed:
                  activity.completed,
              };
            }

            const alreadyMatched =
              (
                skillGap.current_matching_skills ||
                []
              ).some(
                (item) =>
                  item.toLowerCase() ===
                  skill.toLowerCase()
              );

            if (alreadyMatched) {
              return {
                skill,

                score: 85,

                completed: true,
              };
            }

            return {
              skill,

              score: 0,

              completed: false,
            };
          });

        const response = await fetch(
          `${API}/progress/report`,
          {
            method: "POST",

            headers: {
              "Content-Type":
                "application/json",
            },

            body: JSON.stringify({
              required_skills:
                requiredSkills,

              progress,
            }),
          }
        );

        const data =
          await response.json();

        if (!response.ok) {
          throw new Error(
            data.detail ||
              "Progress report failed"
          );
        }

        setProgressReport(data);

        setTimeout(() => {
          document
            .getElementById("progress")
            ?.scrollIntoView({
              behavior: "smooth",
            });
        }, 100);
      } catch (error) {
        console.error(error);

        alert(error.message);
      }
    };

  // -----------------------------
  // ADAPTIVE PLAN
  // -----------------------------

  const generateAdaptivePlan =
    async () => {
      if (!skillGap) {
        alert(
          "Analyze your profile first."
        );

        return;
      }

      const results =
        skillGap.required_skills.map(
          (skill) => {
            const activity =
              activities.find(
                (item) =>
                  item.skill.toLowerCase() ===
                  skill.toLowerCase()
              );

            if (activity) {
              return {
                skill,

                score: activity.score,

                completed:
                  activity.completed,
              };
            }

            return {
              skill,

              score: 0,

              completed: false,
            };
          }
        );

      try {
        const response = await fetch(
          `${API}/adaptive/plan`,
          {
            method: "POST",

            headers: {
              "Content-Type":
                "application/json",
            },

            body: JSON.stringify({
              results,
            }),
          }
        );

        const data =
          await response.json();

        if (!response.ok) {
          throw new Error(
            data.detail ||
              "Adaptive AI failed"
          );
        }

        setAdaptive(data);

        setTimeout(() => {
          document
            .getElementById("adaptive")
            ?.scrollIntoView({
              behavior: "smooth",
            });
        }, 100);
      } catch (error) {
        console.error(error);

        alert(error.message);
      }
    };

  // -----------------------------
  // LEARNING Q&A
  // -----------------------------

  const askQuestion = async () => {
    if (!qaQuestion.trim()) return;

    if (!skillGap) {
      alert(
        "Analyze your profile first."
      );

      return;
    }

    try {
      const response = await fetch(
        `${API}/learning-qa/ask`,
        {
          method: "POST",

          headers: {
            "Content-Type":
              "application/json",
          },

          body: JSON.stringify({
            question: qaQuestion,

            target_role: role,

            skill_gap: skillGap,

            progress_report:
              progressReport,
          }),
        }
      );

      const data =
        await response.json();

      if (!response.ok) {
        throw new Error(
          data.detail ||
            "Learning Q&A failed"
        );
      }

      setQaAnswer(data);
    } catch (error) {
      console.error(error);

      alert(error.message);
    }
  };

  const askSuggestedQuestion =
    (question) => {
      setQaQuestion(question);

      setTimeout(() => {
        document
          .getElementById("qa-input")
          ?.scrollIntoView({
            behavior: "smooth",
          });
      }, 50);
    };

  return (
    <div className="app">

      {/* SIDEBAR */}

      <aside className="sidebar">

        <div className="brand">

          <div className="brand-icon">
            E
          </div>

          <div>
            <h2>EduPath AI</h2>

            <span>
              Learning Agent
            </span>
          </div>

        </div>

        <nav>

          <a href="#dashboard">
            Dashboard
          </a>

          <a href="#profile">
            Profile
          </a>

          <a href="#skills">
            Skill Gap
          </a>

          <a href="#roadmap">
            Roadmap
          </a>

          <a href="#practice">
            Practice
          </a>

          <a href="#progress">
            Progress
          </a>

          <a href="#adaptive">
            Adaptive AI
          </a>

          <a href="#qa">
            Learning Q&A
          </a>

        </nav>

        <div className="agent-box">

          <div className="pulse"></div>

          <strong>
            AI Agent Active
          </strong>

          <p>
            Personalizing your learning
            journey
          </p>

        </div>

      </aside>

      {/* MAIN */}

      <main className="main">

        {/* HEADER */}

        <header className="topbar">

          <div>

            <p className="eyebrow">
              PERSONALIZED LEARNING
            </p>

            <h1>
              Your Learning Journey
            </h1>

            <p className="subtitle">
              Discover your skill gaps and
              follow an AI-powered roadmap.
            </p>

          </div>

          <div className="status">
            <span></span>

            System Online
          </div>

        </header>

        {/* HERO */}

        <section
          className="hero"
          id="dashboard"
        >

          <div>

            <p className="hero-label">
              AI CAREER COACH
            </p>

            <h2>
              Build the skills for your
              dream career.
            </h2>

            <p>
              EduPath AI combines your
              resume, portfolio,
              certificates and projects
              to identify skill gaps,
              create learning objectives,
              generate a roadmap and adapt
              it using your performance.
            </p>

          </div>

          <div className="hero-mark">
            AI
          </div>

        </section>

        {/* ERROR */}

        {errorMessage && (

          <section
            className="card"
            style={{
              border:
                "1px solid #fecaca",

              background:
                "#fef2f2",
            }}
          >

            <strong>
              Backend error:
            </strong>{" "}

            {errorMessage}

          </section>

        )}

        {/* PROFILE */}

        <section
          className="card"
          id="profile"
        >

          <div className="section-title">

            <div>

              <h2>
                1. Profile Intelligence
              </h2>

              <p>
                Add your career context so
                the agent can personalize
                your journey.
              </p>

            </div>

          </div>

          <div className="form-grid">

            <div>

              <label>Name</label>

              <input
                value={profile.name}
                placeholder="Your name"
                onChange={(e) =>
                  setProfile({
                    ...profile,

                    name:
                      e.target.value,
                  })
                }
              />

            </div>

            <div>

              <label>Email</label>

              <input
                type="email"
                value={profile.email}
                placeholder="your@email.com"
                onChange={(e) =>
                  setProfile({
                    ...profile,

                    email:
                      e.target.value,
                  })
                }
              />

            </div>

            <div>

              <label>
                Experience Level
              </label>

              <select
                value={
                  profile.experience_level
                }
                onChange={(e) =>
                  setProfile({
                    ...profile,

                    experience_level:
                      e.target.value,
                  })
                }
              >

                <option>
                  Beginner
                </option>

                <option>
                  Intermediate
                </option>

                <option>
                  Advanced
                </option>

              </select>

            </div>

            <div>

              <label>
                Weekly Study Hours
              </label>

              <input
                type="number"
                min="1"
                max="60"
                value={
                  profile.study_hours
                }
                onChange={(e) =>
                  setProfile({
                    ...profile,

                    study_hours:
                      Number(
                        e.target.value
                      ),
                  })
                }
              />

            </div>

          </div>

          <div
            style={{
              marginTop: "16px",
            }}
          >

            <label>
              Career Goal
            </label>

            <textarea
              rows="3"
              value={
                profile.career_goal
              }
              placeholder="Example: I want to become a Data Scientist and build strong ML skills."
              onChange={(e) =>
                setProfile({
                  ...profile,

                  career_goal:
                    e.target.value,
                })
              }
            />

          </div>

        </section>

        {/* PORTFOLIO */}

        <section className="card">

          <div className="section-title">

            <div>

              <h2>
                2. Portfolio Intelligence
              </h2>

              <p>
                Add your portfolio/GitHub
                and describe your work.
              </p>

            </div>

          </div>

          <div className="form-grid">

            <div>

              <label>
                Portfolio / GitHub URL
              </label>

              <input
                type="url"
                value={portfolio.url}
                placeholder="https://github.com/username"
                onChange={(e) =>
                  setPortfolio({
                    ...portfolio,

                    url:
                      e.target.value,
                  })
                }
              />

            </div>

            <div>

              <label>
                Portfolio Description
              </label>

              <input
                value={
                  portfolio.description
                }
                placeholder="Python, SQL, Power BI, Machine Learning..."
                onChange={(e) =>
                  setPortfolio({
                    ...portfolio,

                    description:
                      e.target.value,
                  })
                }
              />

            </div>

          </div>

        </section>

        {/* CERTIFICATES */}

        <section className="card">

          <div className="section-title">

            <div>

              <h2>
                3. Certificates
              </h2>

              <p>
                Add certifications and
                courses.
              </p>

            </div>

            <button
              className="secondary-btn"
              onClick={
                addCertificate
              }
            >
              + Add Certificate
            </button>

          </div>

          {certificates.length ===
          0 ? (

            <p className="muted">
              No certificates added.
            </p>

          ) : (

            certificates.map(
              (
                certificate,
                index
              ) => (

                <div
                  key={index}
                  className="row-box"
                >

                  <div className="form-grid">

                    <div>

                      <label>
                        Certificate
                      </label>

                      <input
                        value={
                          certificate.name
                        }
                        placeholder="IBM Data Analyst"
                        onChange={(e) =>
                          updateCertificate(
                            index,
                            "name",
                            e.target.value
                          )
                        }
                      />

                    </div>

                    <div>

                      <label>
                        Platform
                      </label>

                      <input
                        value={
                          certificate.platform
                        }
                        placeholder="Coursera"
                        onChange={(e) =>
                          updateCertificate(
                            index,
                            "platform",
                            e.target.value
                          )
                        }
                      />

                    </div>

                    <div>

                      <label>
                        Status
                      </label>

                      <select
                        value={
                          certificate.status
                        }
                        onChange={(e) =>
                          updateCertificate(
                            index,
                            "status",
                            e.target.value
                          )
                        }
                      >

                        <option>
                          Completed
                        </option>

                        <option>
                          In Progress
                        </option>

                      </select>

                    </div>

                  </div>

                  <button
                    className="secondary-btn"
                    style={{
                      marginTop: "10px",
                    }}
                    onClick={() =>
                      removeCertificate(
                        index
                      )
                    }
                  >
                    Remove
                  </button>

                </div>

              )
            )

          )}

        </section>

        {/* PROJECTS */}

        <section className="card">

          <div className="section-title">

            <div>

              <h2>
                4. Project Intelligence
              </h2>

              <p>
                Projects help the agent
                understand practical
                experience.
              </p>

            </div>

            <button
              className="secondary-btn"
              onClick={addProject}
            >
              + Add Project
            </button>

          </div>

          {projects.map(
            (project, index) => (

              <div
                key={index}
                className="row-box"
              >

                <div className="form-grid">

                  <div>

                    <label>
                      Project Title
                    </label>

                    <input
                      value={
                        project.title
                      }
                      placeholder="Customer Churn Prediction"
                      onChange={(e) =>
                        updateProject(
                          index,
                          "title",
                          e.target.value
                        )
                      }
                    />

                  </div>

                  <div>

                    <label>
                      Technologies
                    </label>

                    <input
                      value={
                        project.technologies
                      }
                      placeholder="Python, Pandas, Scikit-learn"
                      onChange={(e) =>
                        updateProject(
                          index,
                          "technologies",
                          e.target.value
                        )
                      }
                    />

                  </div>

                </div>

                <div
                  style={{
                    marginTop: "12px",
                  }}
                >

                  <label>
                    Description
                  </label>

                  <textarea
                    rows="3"
                    value={
                      project.description
                    }
                    placeholder="Describe what you built and what problem it solved."
                    onChange={(e) =>
                      updateProject(
                        index,
                        "description",
                        e.target.value
                      )
                    }
                  />

                </div>

                {projects.length >
                  1 && (

                  <button
                    className="secondary-btn"
                    style={{
                      marginTop:
                        "10px",
                    }}
                    onClick={() =>
                      removeProject(
                        index
                      )
                    }
                  >
                    Remove Project
                  </button>

                )}

              </div>

            )
          )}

        </section>

        {/* RESUME */}

        <section className="card upload-card">

          <div className="section-title">

            <div>

              <h2>
                5. Analyze Your Profile
              </h2>

              <p>
                Upload your resume and
                choose your target role.
              </p>

            </div>

          </div>

          <div className="upload-grid">

            <label className="file-box">

              <input
                type="file"
                accept=".pdf"
                onChange={(e) =>
                  setResume(
                    e.target.files?.[0] ||
                      null
                  )
                }
              />

              <div className="upload-icon">
                ↑
              </div>

              <strong>
                {resume
                  ? resume.name
                  : "Upload your PDF resume"}
              </strong>

              <span>
                {resume
                  ? "Resume selected"
                  : "Drag & drop or click to browse"}
              </span>

            </label>

            <div className="role-box">

              <label>
                Target Career Role
              </label>

              <select
                value={role}
                onChange={(e) =>
                  setRole(
                    e.target.value
                  )
                }
              >

                {ROLE_OPTIONS.map(
                  (item) => (
                    <option
                      key={item}
                    >
                      {item}
                    </option>
                  )
                )}

              </select>

              <button
                className="primary-btn"
                onClick={
                  uploadResume
                }
                disabled={
                  !resume ||
                  loading
                }
              >
                {loading
                  ? "Analyzing..."
                  : "Analyze My Profile →"}
              </button>

            </div>

          </div>

          {analysisComplete && (

            <div
              className="success-box"
            >

              <strong>
                Profile analyzed
                successfully.
              </strong>

              <p>
                Resume skills, portfolio,
                certificates and projects
                were combined before
                skill-gap analysis.
              </p>

            </div>

          )}

        </section>

        {/* SKILL GAP */}

        {skillGap && (

          <>

            <section
              className="stats-grid"
              id="skills"
            >

              <div className="stat-card">

                <span>
                  Career Readiness
                </span>

                <strong>
                  {
                    skillGap.readiness_percentage
                  }%
                </strong>

                <small>
                  Based on required skills
                </small>

              </div>

              <div className="stat-card">

                <span>
                  Skills Matched
                </span>

                <strong>
                  {
                    skillGap.matched_count
                  }
                </strong>

                <small>
                  Existing relevant skills
                </small>

              </div>

              <div className="stat-card">

                <span>
                  Skill Gaps
                </span>

                <strong>
                  {
                    skillGap.missing_count
                  }
                </strong>

                <small>
                  Skills to develop
                </small>

              </div>

              <div className="stat-card">

                <span>
                  Priority
                </span>

                <strong>
                  {
                    skillGap.overall_priority
                  }
                </strong>

                <small>
                  Learning priority
                </small>

              </div>

            </section>

            <section className="card">

              <div className="section-title">

                <div>

                  <h2>
                    Skill Gap Analysis
                  </h2>

                  <p>
                    Target role:{" "}
                    <strong>
                      {
                        skillGap.target_role
                      }
                    </strong>
                  </p>

                </div>

                <button
                  className="secondary-btn"
                  onClick={
                    generateProgressReport
                  }
                >
                  Generate Progress
                  Report →
                </button>

              </div>

              <div className="skill-columns">

                <div>

                  <h3 className="green-title">
                    ✓ Current Skills
                  </h3>

                  <div className="chips">

                    {skillGap.current_matching_skills.map(
                      (skill) => (

                        <span
                          className="chip green"
                          key={skill}
                        >
                          {skill}
                        </span>

                      )
                    )}

                  </div>

                </div>

                <div>

                  <h3 className="orange-title">
                    ! Skills to Learn
                  </h3>

                  <div className="chips">

                    {skillGap.missing_skills.map(
                      (skill) => (

                        <span
                          className="chip orange"
                          key={skill}
                        >
                          {skill}
                        </span>

                      )
                    )}

                  </div>

                </div>

              </div>

              {combinedSkills.length >
                0 && (

                <div
                  className="source-box"
                >

                  <strong>
                    Profile Intelligence
                    Skills
                  </strong>

                  <p>
                    {combinedSkills.join(
                      " • "
                    )}
                  </p>

                </div>

              )}

            </section>

          </>

        )}

        {/* ROADMAP */}

        {roadmap && (

          <section
            className="card"
            id="roadmap"
          >

            <div className="section-title">

              <div>

                <h2>
                  Personalized 4-Week
                  Roadmap
                </h2>

                <p>
                  {
                    roadmap.roadmap
                      ?.total_weeks || 4
                  }{" "}
                  weeks ·{" "}
                  {
                    roadmap.roadmap
                      ?.hours_per_week ||
                    profile.study_hours ||
                    10
                  }{" "}
                  hours/week
                </p>

              </div>

            </div>

            <div className="timeline">

              {roadmap.roadmap?.roadmap?.map(
                (week) => (

                  <div
                    className="week"
                    key={week.week}
                  >

                    <div className="week-number">
                      W{week.week}
                    </div>

                    <div className="week-content">

                      <h3>
                        {week.focus.join(
                          " + "
                        )}
                      </h3>

                      {week.learning_tasks.map(
                        (
                          task,
                          index
                        ) => {

                          const activity =
                            activities.find(
                              (item) =>
                                item.skill.toLowerCase() ===
                                task.topic.toLowerCase()
                            );

                          return (

                            <div
                              className="task"
                              key={index}
                            >

                              <span>
                                {activity
                                  ? "✓"
                                  : "○"}
                              </span>

                              <div
                                style={{
                                  flex: 1,
                                }}
                              >

                                <strong>
                                  {
                                    task.topic
                                  }
                                </strong>

                                <small>
                                  {
                                    task.estimated_hours
                                  }{" "}
                                  hours

                                  {activity
                                    ? ` · Score ${activity.score}%`
                                    : ""}
                                </small>

                                <div
                                  className="task-action"
                                >

                                  <input
                                    type="number"
                                    min="0"
                                    max="100"
                                    placeholder="Score"
                                    id={`score-${week.week}-${index}`}
                                    className="score-input"
                                  />

                                  <button
                                    className="secondary-btn"
                                    onClick={() => {

                                      const input =
                                        document.getElementById(
                                          `score-${week.week}-${index}`
                                        );

                                      completeActivity(
                                        task.topic,
                                        input?.value ||
                                          75
                                      );

                                    }}
                                  >
                                    {activity
                                      ? "Update Score"
                                      : "Complete"}
                                  </button>

                                </div>

                              </div>

                            </div>

                          );

                        }
                      )}

                      <div className="practice-highlight">

                        <strong>
                          Practice:
                        </strong>{" "}

                        {
                          week.practice_task
                        }

                      </div>

                    </div>

                  </div>

                )
              )}

            </div>

          </section>

        )}

        {/* PRACTICE */}

        {practice && (

          <section
            className="card"
            id="practice"
          >

            <div className="section-title">

              <div>

                <h2>
                  AI Practice Tasks
                </h2>

                <p>
                  Hands-on tasks generated
                  for your skill gaps.
                </p>

              </div>

            </div>

            <div className="practice-grid">

              {practice.practice?.map(
                (item) => (

                  <div
                    className="practice-card"
                    key={item.skill}
                  >

                    <div className="practice-header">

                      <h3>
                        {item.skill}
                      </h3>

                      <span>
                        {item.difficulty}
                      </span>

                    </div>

                    <ol>

                      {item.tasks.map(
                        (
                          task,
                          index
                        ) => (

                          <li key={index}>
                            {task}
                          </li>

                        )
                      )}

                    </ol>

                    <div className="mini-project">

                      <strong>
                        Mini Project
                      </strong>

                      <p>
                        {
                          item.mini_project
                        }
                      </p>

                    </div>

                    <div className="practice-complete">

                      <input
                        type="number"
                        min="0"
                        max="100"
                        placeholder="Score 0-100"
                        id={`practice-${item.skill}`}
                        className="score-input"
                      />

                      <button
                        className="primary-btn"
                        onClick={() => {

                          const input =
                            document.getElementById(
                              `practice-${item.skill}`
                            );

                          completeActivity(
                            item.skill,
                            input?.value ||
                              75
                          );

                        }}
                      >
                        Mark Completed
                      </button>

                    </div>

                  </div>

                )
              )}

            </div>

          </section>

        )}

        {/* PROGRESS */}

        {progressReport && (

          <section
            className="card"
            id="progress"
          >

            <div className="section-title">

              <div>

                <h2>
                  Learning Progress Report
                </h2>

                <p>
                  Generated from your
                  activities and current
                  profile skills.
                </p>

              </div>

              <strong>
                {
                  progressReport.overall_progress_percentage
                }
                % Complete
              </strong>

            </div>

            <div className="progress-summary">

              <div>

                <span>
                  Acquired
                </span>

                <strong>
                  {
                    progressReport
                      .summary
                      .acquired_count
                  }
                </strong>

              </div>

              <div>

                <span>
                  In Progress
                </span>

                <strong>
                  {
                    progressReport
                      .summary
                      .in_progress_count
                  }
                </strong>

              </div>

              <div>

                <span>
                  Remaining
                </span>

                <strong>
                  {
                    progressReport
                      .summary
                      .remaining_count
                  }
                </strong>

              </div>

            </div>

            <div className="progress-columns">

              <div>

                <h3 className="green-title">
                  ✓ Acquired Skills
                </h3>

                {progressReport
                  .acquired_skills
                  .length === 0 ? (

                  <p className="muted">
                    No skills acquired
                    yet.
                  </p>

                ) : (

                  progressReport.acquired_skills.map(
                    (item) => (

                      <div
                        className="progress-item"
                        key={item.skill}
                      >

                        <strong>
                          {item.skill}
                        </strong>

                        <span>
                          {item.score}%
                        </span>

                      </div>

                    )
                  )

                )}

              </div>

              <div>

                <h3 className="orange-title">
                  ◐ In Progress
                </h3>

                {progressReport
                  .skills_in_progress
                  .length === 0 ? (

                  <p className="muted">
                    No skills currently
                    in progress.
                  </p>

                ) : (

                  progressReport.skills_in_progress.map(
                    (item) => (

                      <div
                        className="progress-item"
                        key={item.skill}
                      >

                        <strong>
                          {item.skill}
                        </strong>

                        <span>
                          {item.score}%
                        </span>

                      </div>

                    )
                  )

                )}

              </div>

              <div>

                <h3>
                  ○ Remaining
                </h3>

                {progressReport
                  .remaining_skills
                  .length === 0 ? (

                  <p className="muted">
                    No remaining skills.
                  </p>

                ) : (

                  progressReport.remaining_skills.map(
                    (skill) => (

                      <div
                        className="progress-item"
                        key={skill}
                      >

                        <strong>
                          {skill}
                        </strong>

                        <span>
                          0%
                        </span>

                      </div>

                    )
                  )

                )}

              </div>

            </div>

            <div className="next-steps">

              <h3>
                Next Steps
              </h3>

              {progressReport.next_steps.map(
                (step, index) => (

                  <p key={index}>
                    → {step}
                  </p>

                )
              )}

            </div>

          </section>

        )}

        {/* ADAPTIVE */}

        <section
          className="card adaptive-card"
          id="adaptive"
        >

          <div className="section-title">

            <div>

              <h2>
                Adaptive Learning Agent
              </h2>

              <p>
                The roadmap changes based
                on your learning performance.
              </p>

            </div>

            <button
              className="secondary-btn"
              onClick={
                generateAdaptivePlan
              }
            >
              Recalculate Adaptive Plan
            </button>

          </div>

          {adaptive ? (

            adaptive.results ? (

              <div>

                <div className="adaptive-message">

                  <strong>
                    {
                      adaptive.overall_action
                    }
                  </strong>

                </div>

                <div className="adaptive-grid">

                  {adaptive.results.map(
                    (result) => (

                      <div
                        className="adaptive-item"
                        key={result.skill}
                      >

                        <div>

                          <strong>
                            {result.skill}
                          </strong>

                          <small>
                            {
                              result.recommendation
                            }
                          </small>

                        </div>

                        <div
                          className={`score ${result.status}`}
                        >
                          {result.score}%
                        </div>

                      </div>

                    )
                  )}

                </div>

              </div>

            ) : (

              <div className="adaptive-message">

                <strong>
                  {adaptive.status}
                </strong>

                <p>
                  {adaptive.message}
                </p>

              </div>

            )

          ) : (

            <div className="empty-state">

              Complete a learning task
              and click{" "}

              <strong>
                Recalculate Adaptive Plan
              </strong>

            </div>

          )}

        </section>

        {/* Q&A */}

        <section
          className="card"
          id="qa"
        >

          <div className="section-title">

            <div>

              <h2>
                Learning Journey Q&A
              </h2>

              <p>
                Ask the agent about your
                skill gaps, progress and
                next learning step.
              </p>

            </div>

          </div>

          <div className="suggestions">

            {[
              "What should I learn next?",
              "Why am I not ready for Data Scientist?",
              "What are my skill gaps?",
              "Show my progress",
            ].map(
              (question) => (

                <button
                  key={question}
                  className="secondary-btn"
                  onClick={() =>
                    askSuggestedQuestion(
                      question
                    )
                  }
                >
                  {question}
                </button>

              )
            )}

          </div>

          <div
            id="qa-input"
            className="qa-row"
          >

            <input
              value={qaQuestion}
              placeholder="Ask your learning journey question..."
              onChange={(e) =>
                setQaQuestion(
                  e.target.value
                )
              }
              onKeyDown={(e) => {

                if (
                  e.key === "Enter"
                ) {
                  askQuestion();
                }

              }}
            />

            <button
              className="primary-btn"
              onClick={
                askQuestion
              }
            >
              Ask AI →
            </button>

          </div>

          {qaAnswer && (

            <div className="answer-box">

              <div className="answer-label">
                EDUPATH AI
              </div>

              <h3>
                {qaAnswer.question}
              </h3>

              <p>
                {qaAnswer.answer}
              </p>

              <div className="answer-meta">

                <span>
                  Readiness:{" "}
                  {
                    qaAnswer.readiness_percentage
                  }%
                </span>

                <span>
                  Gaps:{" "}
                  {
                    qaAnswer
                      .missing_skills
                      ?.length || 0
                  }
                </span>

              </div>

            </div>

          )}

        </section>

        <footer>

          <strong>
            EduPath AI
          </strong>{" "}
          · Personalized Learning &
          Skill Gap Agent · Hackathon
          2026

        </footer>

      </main>

    </div>
  );
}

export default App;