import { useState } from "react";

import FormInput from "./FormInput";
import FormSelect from "./FormSelect";

import {
  genderOptions,
  chestPainOptions,
  fastingBloodSugarOptions,
  restECGOptions,
  exerciseAnginaOptions,
  slopeOptions,
  vesselOptions,
  thalOptions,
} from "../constants/patientOptions";

export default function PatientForm({onSubmit}) {
  const [formData, setFormData] = useState({
    age: "",
    sex: 1,
    cp: 0,
    trestbps: "",
    chol: "",
    fbs: 0,
    restecg: 0,
    thalach: "",
    exang: 0,
    oldpeak: "",
    slope: 0,
    ca: 0,
    thal: 1,
  });

  const handleChange = (e) => {
    setFormData({
      ...formData,
      [e.target.name]: Number(e.target.value),
    });
  };

  return (
    <div className="bg-white rounded-2xl shadow-lg p-8 mt-8 max-w-5xl w-full">

      <h2 className="text-2xl font-semibold mb-6">
        Patient Information
      </h2>

      <div className="grid md:grid-cols-2 gap-5">

        <FormInput
          label="Age"
          name="age"
          value={formData.age}
          placeholder="Enter age"
          onChange={handleChange}
        />

        <FormSelect
          label="Gender"
          name="sex"
          value={formData.sex}
          options={genderOptions}
          onChange={handleChange}
        />

        <FormSelect
          label="Chest Pain Type"
          name="cp"
          value={formData.cp}
          options={chestPainOptions}
          onChange={handleChange}
        />

        <FormInput
          label="Resting Blood Pressure (mmHg)"
          name="trestbps"
          value={formData.trestbps}
          placeholder="120"
          onChange={handleChange}
        />

        <FormInput
          label="Serum Cholesterol (mg/dL)"
          name="chol"
          value={formData.chol}
          placeholder="200"
          onChange={handleChange}
        />

        <FormSelect
          label="Fasting Blood Sugar"
          name="fbs"
          value={formData.fbs}
          options={fastingBloodSugarOptions}
          onChange={handleChange}
        />

        <FormSelect
          label="Resting ECG Results"
          name="restecg"
          value={formData.restecg}
          options={restECGOptions}
          onChange={handleChange}
        />

        <FormInput
          label="Maximum Heart Rate Achieved"
          name="thalach"
          value={formData.thalach}
          placeholder="150"
          onChange={handleChange}
        />

        <FormSelect
          label="Exercise-Induced Angina"
          name="exang"
          value={formData.exang}
          options={exerciseAnginaOptions}
          onChange={handleChange}
        />

        <FormInput
          label="ST Depression (Oldpeak)"
          name="oldpeak"
          value={formData.oldpeak}
          placeholder="1.2"
          onChange={handleChange}
        />

        <FormSelect
          label="Slope of Peak Exercise ST Segment"
          name="slope"
          value={formData.slope}
          options={slopeOptions}
          onChange={handleChange}
        />

        <FormSelect
          label="Number of Major Vessels"
          name="ca"
          value={formData.ca}
          options={vesselOptions}
          onChange={handleChange}
        />

        <FormSelect
          label="Thalassemia"
          name="thal"
          value={formData.thal}
          options={thalOptions}
          onChange={handleChange}
        />

      </div>

      <button
        type="button"
        onClick={() => onSubmit(formData)}
        className="
            mt-8
            w-full
            rounded-2xl
            bg-red-600
            px-6
            py-4
            text-lg
            font-bold
            text-white
            shadow-lg
            transition-all
            duration-300
            hover:bg-red-700
            hover:shadow-xl
            hover:scale-[1.02]
            active:scale-95
        "
        >
        ❤️ Predict Heart Disease
    </button>

    </div>
  );
}