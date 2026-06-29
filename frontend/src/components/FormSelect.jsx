export default function FormSelect({
  label,
  name,
  value,
  options,
  onChange,
}) {
  return (
    <div className="flex flex-col">
      <label className="mb-2 font-medium text-gray-700">
        {label}
      </label>

      <select
        name={name}
        value={value}
        onChange={onChange}
        className="border rounded-lg p-3 focus:outline-none focus:ring-2 focus:ring-red-500"
      >
        {options.map((option) => (
          <option
            key={option.value}
            value={option.value}
          >
            {option.label}
          </option>
        ))}
      </select>
    </div>
  );
}