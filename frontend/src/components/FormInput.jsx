export default function FormInput({
  label,
  name,
  type = "number",
  placeholder,
  value,
  onChange,
}) {
  return (
    <div className="flex flex-col">
      <label className="mb-2 font-medium text-gray-700">
        {label}
      </label>

      <input
        type={type}
        name={name}
        value={value}
        placeholder={placeholder}
        onChange={onChange}
        className="border rounded-lg p-3 focus:outline-none focus:ring-2 focus:ring-red-500"
      />
    </div>
  );
}